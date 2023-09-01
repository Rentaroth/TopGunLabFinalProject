from app.repositories.comment_repository import CommentRepository
from app.serializers import CommentSerializer
from app.services.user_service import UserService
from app.services.post_service import PostService

from django.utils import timezone
from django.forms import model_to_dict
from bson import ObjectId

class CommentService(CommentRepository):
  serializer = CommentSerializer
  def __init__(self, id=None, comment=None, user_id=None, post_id=None):
    super().__init__()
    self.id = id
    self.comment = comment
    self.user_id = user_id
    self.post_id = post_id

  def CommentCreationService(self):
    data = {
      'comment': self.comment,
      'user_id': self.user_id,
      'post_id': self.post_id,
      'created_at': timezone.now().__str__(),
      # 'updated_at': timezone.now().__str__(),
    }
    validator =  self.serializer(data=data)
    if validator.is_valid():
      validated = dict(validator.validated_data)
      validated.update({
        'created_at': validator['created_at'].__str__(),
      })
      user_instance = UserService(id=validated['user_id'])
      user_obj = user_instance.user_object_obtention(user_instance)
      post_instance = PostService(id=validated['post_id'])
      post_obj = post_instance.post_object_obtention()
      validated.update({
        'user_id': user_obj,
        'post_id': post_obj,
      })
      try:
        obj = self.create.delay(self, self.model, validated)
        result = obj.get(timeout=None)
        result = model_to_dict(result)
        print(result)
        result.update({
          '_id': result['_id'].__str__(),
          'user_id': result['user_id'].__str__(),
          'post_id': result['post_id'].__str__(),
        })
        return result
      except Exception as err:
        print(err)


  def CommentGetService(self):
    id = ObjectId(self.id)
    try:
      obj = self.read.delay(self, self.model, id)
      result = obj.get(timeout=None)
      res = model_to_dict(result)
      res.update({
        '_id': str(res['_id']),
        'user_id': str(res['user_id']),
        'post_id': str(res['post_id']),
      })
      return res
    except Exception as error:
      print(error)

  def CommentUpdateService(self):
    id = ObjectId(self.id)
    data = {
      'comment': self.comment,
    }
    validator = self.serializer(data=data, partial=True)
    if validator.is_valid():
      validated = dict(validator.validated_data)
      
      try:
        obj = self.update.delay(self, self.model, validated, id)
        result = obj.get(timeout=None)
        res = model_to_dict(result)
        res.update({
          '_id': str(res['_id']),
          'user_id': str(res['user_id']),
          'post_id': str(res['post_id']),
        })
        return res
      except Exception as error:
        print(error)

  def CommentDeleteService(self):
    id = ObjectId(self.id)
    obj = self.delete.delay(self, self.model, id)
    result = obj.get(timeout=None)
    return result
