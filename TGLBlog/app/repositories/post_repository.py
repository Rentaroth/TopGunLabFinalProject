from app.models import *
from .base_repository import BaseRepository
from app.models import Posts
from django.db.models import Q

class PostRepository(BaseRepository):
  model = Posts
  def __init__(self):
    super().__init__()

  def post_object_obtention(self):
    id = ObjectId(self.id)
    obj = self.read.delay(self, self.model, id)
    result = obj.get(timeout=None)
    return result

  def post_search(self, filters):
    result = self.model.objects.filter(Q(title__icontains=filters['title']) & Q(created_at__range=(filters['start_date'], filters['end_date'])))
    return result