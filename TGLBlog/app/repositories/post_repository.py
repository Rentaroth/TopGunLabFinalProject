from app.models import *
from .base_repository import BaseRepository
from app.models import Posts

class PostRepository(BaseRepository):
  model = Posts
  def __init__(self):
    super().__init__()

  def post_objcet_obtention(self):
    id = ObjectId(self.id)
    obj = self.read.delay(self, self.model, id)
    result = obj.get(timeout=None)
    return result

  def post_search(self, content):
    obj = self.model.objects.filter()