from app.repositories.likes_repository import LikesRepository
from app.serializers import PostsLikesSerializer
from .user_service import UserService
from .post_service import PostService

from django.forms import model_to_dict

class LikesService(LikesRepository):
  serializer = PostsLikesSerializer
  def __init__(self, user_id=None, post_id=None):
    super().__init__()
    self.id = id
    self.user_id = user_id
    self.post_id = post_id

  def LikesCreationService(self):
    data = {
      'user_id': self.user_id,
      'post_id': self.post_id,
    }
    validator = self.serializer(data=data)
    if validator.is_valid():
      validated = validator.validated_data
      is_unique = self.verify_like_existance(validated['user_id'], validated['post_id'])
      if is_unique:
        user_entity = UserService(id=validated['user_id'])
        user = user_entity.user_object_obtention(user_entity)
        post_entity = PostService(id=validated['post_id'])
        post = post_entity.post_object_obtention()
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
        raise Exception('Cannot like twice.')
    else:
      print(validator.error_messages)
      raise ValueError("Data can't be validated.")