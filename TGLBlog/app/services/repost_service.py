from app.repositories.repost_repository import RepostRepository
from app.serializers import RepostSerializer
from .user_service import UserService
from .post_service import PostService

from django.utils import timezone
from django.forms import model_to_dict

class RepostService(RepostRepository):
  serializer = RepostSerializer
  def __init__(self, user_id=None, post_id=None):
    super().__init__()
    self.id = id
    self.user_id = user_id
    self.post_id = post_id

  def RepostCreationService(self):
    data = {
      'user_id': self.user_id,
      'post_id': self.post_id,
    }
    validator = self.serializer(data=data)
    if validator.is_valid():
      validated = validator.validated_data
      is_unique = self.verify_existance(validated['user_id'], validated['post_id'])
      if is_unique:
        user_entity = UserService(id=validated['user_id'])
        user = user_entity.user_object_obtention.delay(user_entity)
        post_entity = PostService(id=validated['post_id'])
        post = post_entity.post_object_obtention()
        user = user.get(timeout=None)
        validated.update({
          'user_id': user,
          'post_id': post,
        })
        async_obj = self.create.delay(self, self.model, validated)
        result = async_obj.get(timeout=None)
        result = model_to_dict(result)
        result.update({
          '_id': result['_id'].__str__(),
          'user_id': result['user_id'].__str__(),
          'post_id': result['post_id'].__str__(),
        })
        return result
      else:
        raise Exception('Cannot repost twice.')
    else:
      print(validator.error_messages)
      raise ValueError("Data can't be validated.")
