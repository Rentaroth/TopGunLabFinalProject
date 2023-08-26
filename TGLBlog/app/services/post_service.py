from app.repositories.post_repository import PostRepository
from app.serializers import PostSerializer
from .user_service import UserService

from django.utils import timezone
from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.forms import model_to_dict
from bson import ObjectId

class PostService(PostRepository):
  serializer = PostSerializer
  def __init__(self, id = None, title= None, content = None, status = None, user_id = None, category_id = None):
    super().__init__()
    self.id = id
    self.title = title
    self.content = content
    self.status = status
    self.user_id = user_id
    self.category_id = category_id

  def PostCreationService(self):
    created = timezone.now()
    updated = timezone.now()
    data = {
      'title': self.title,
      'content': self.content,
      'status': self.status,
      'user_id': self.user_id,
      #'category_id': self.category_id,
      'created_at': created.__str__(),
      'updated_at': updated.__str__(),
    }
    validator = self.serializer(data=data)
    if validator.is_valid():
      validated = dict(validator.validated_data)
      user_instance = UserService(id=self.user_id)
      user_obj = user_instance.user_objcet_obtention()
      validated.update({
        'user_id': user_obj,
        # 'category_id': ObjectId(self.category_id),
        'created_at': validator.validated_data['created_at'].__str__(),
        'updated_at': validator.validated_data['updated_at'].__str__(),
      })
      creation_task = self.create.delay(self, self.model, validated)
      result = creation_task.get(timeout=None)
      result['user_id'] = self.user_id
      return result
    else:
      print(validator.error_messages)
      raise ValueError("Data can't be validated!")
  
  def PostGetService(self):
    id = ObjectId(self.id)
    obj = self.read.delay(self, self.model, id)
    result = obj.get(timeout=None)
    res = model_to_dict(result)
    res['_id'] = res['_id'].__str__()
    res['user_id'] = res['user_id'].__str__()
    return res

  def PostUpdateService(self):
    id = ObjectId(self.id)
    updated = timezone.now()
    data_collector = {
      'title': self.title,
      'content': self.content,
      'status': self.status,
      'user_id': self.user_id,
      # 'category_id': self.category_id,
      'updated_at': updated.__str__(),
    }
    data = {i:j for i, j in data_collector.items() if j is not None}
    try:
      validator = self.serializer(data=data, partial=True)
      if validator.is_valid():
        validated = dict(validator.validated_data)
        result = self.update.delay(self, self.model, validated, id)
        res = result.get(timeout=None)
        res = model_to_dict(res)
        res['_id'] = res['_id'].__str__()
        res['user_id'] = res['user_id'].__str__()
        return res
    except Exception as error:
      print(error)
      print(validator.error_messages)
      raise ValueError("Data can't be validated!")
  
  def PostDeleteService(self):
    id = ObjectId(self.id)
    obj = self.delete.delay(self, self.model, id)
    result = obj.get(timeout=None)
    return result
    