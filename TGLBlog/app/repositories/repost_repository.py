from app.models import *
from .base_repository import BaseRepository
from app.models import Reposts
from django.db.models import Q
from bson import ObjectId

class RepostRepository(BaseRepository):
  model = Reposts
  def __init__(self):
    super().__init__()

  def verify_existance(self, user_id, post_id):
    user_obj_id = ObjectId(user_id)
    post_obj_id = ObjectId(post_id)
    query = Q(user_id=user_obj_id) & Q(post_id=post_obj_id)

    result = self.model.objects.filter(query)
    res = []
    for obj in result:
      res.append(obj)
    if len(res) > 0:
      return False
    else:
      return True