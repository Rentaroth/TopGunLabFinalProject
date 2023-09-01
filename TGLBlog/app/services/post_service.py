from app.repositories.post_repository import PostRepository
from app.serializers import PostSerializer
from .user_service import UserService
from .category_service import CategoryService
from .tag_service import TagService
from app.utilities.time_parser import tz_parser_nozone

from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.forms import model_to_dict
from bson import ObjectId

class PostService(PostRepository):
  serializer = PostSerializer
  def __init__(self, id = None, title= None, content = None, status = None, user_id = None, category_id = None, tag_id=None, search_title = None, search_start_date = None, search_end_date = None):
    super().__init__()
    self.id = id
    self.title = title
    self.content = content
    self.status = status
    self.user_id = user_id
    self.category_id = category_id
    self.tag_id = tag_id
    self.search_title = search_title
    self.search_start_date = search_start_date
    self.search_end_date = search_end_date

  def PostCreationService(self):
    created = timezone.now()
    updated = timezone.now()
    data = {
      'title': self.title,
      'content': self.content,
      'status': self.status,
      'user_id': self.user_id,
      'category_id': self.category_id,
      'tag_id': self.tag_id,
      'created_at': created.__str__(),
      'updated_at': updated.__str__(),
    }
    validator = self.serializer(data=data)
    if validator.is_valid():
      validated = dict(validator.validated_data)
      user_instance = UserService(id=self.user_id)
      user_obj = user_instance.user_object_obtention.delay(user_instance.self_instance)
      category_instance = CategoryService(id=self.category_id)
      category_obj = category_instance.obtain_one_category.delay(category_instance.self_instance)
      user_obj = user_obj.get(timeout=None)
      category_obj = category_obj.get(timeout=None)
      validated.update({
        'user_id': user_obj,
        'category_id': category_obj,
        'created_at': validator.validated_data['created_at'].__str__(),
        'updated_at': validator.validated_data['updated_at'].__str__(),
      })
      
      async_obj = self.tag_insert.delay(self, validated)
      result = async_obj.get(timeout=None)
      result = model_to_dict(result)
      result.update({
        '_id': result['_id'].__str__(),
        'user_id': result['user_id'].__str__(),
        'category_id': result['category_id'].__str__(),
        'tag_id': self.tag_id
      })
      print(result)
      return result
    else:
      print(validator.error_messages)
      raise ValueError("Data can't be validated!")
  
  def PostGetService(self):
    id = ObjectId(self.id)
    obj = self.read.delay(self, self.model, id)
    result = obj.get(timeout=None)
    res = model_to_dict(result)
    tags = [model_to_dict(x) for x in res['tag_id']]
    tags_parsed = [x['_id'].__str__() for x in tags]
    res.update({
      '_id': res['_id'].__str__(),
      'user_id': res['user_id'].__str__(),
      'category_id': res['category_id'].__str__(),
      'tag_id': tags_parsed,
    })
    return res

  def PostUpdateService(self):
    id = ObjectId(self.id)
    updated = timezone.now()
    data_collector = {
      'title': self.title,
      'content': self.content,
      'status': self.status,
      'user_id': self.user_id,
      'category_id': self.category_id,
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
        tags = [model_to_dict(x) for x in res['tag_id']]
        tags_parsed = [x['_id'].__str__() for x in tags]
        res.update({
          '_id': res['_id'].__str__(),
          'user_id': res['user_id'].__str__(),
          'category_id': res['category_id'].__str__(),
          'tag_id': tags_parsed,
        })
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
    
  def PostSearchService(self):
    filters = {
      'title': self.search_title,
    }
    if self.search_start_date:
      filters.update({
        'start_date': tz_parser_nozone(self.search_start_date),
      })
    else:
      filters.update({
        'start_date': tz_parser_nozone('1990-01-01'),
      })
    if self.search_end_date:
      filters.update({
        'end_date': tz_parser_nozone(self.search_end_date),
      })
    else:
      filters.update({
        'end_date': timezone.now(),
      })

    try:
      obj = self.post_search(filters)
      res = []
      for item in obj:
        res.append({ '_id': str(item._id), 'title': item.title, 'created_at': item.created_at })
      print(res)
      return res
    except ValueError as error:
      print(error)
      return ''

    