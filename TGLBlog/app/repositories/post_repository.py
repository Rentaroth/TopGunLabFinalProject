from app.models import *
from .base_repository import BaseRepository
from app.models import Posts
from django.db.models import Q

class PostRepository(BaseRepository):
  model = Posts
  def __init__(self):
    super().__init__()

  def post_objcet_obtention(self):
    id = ObjectId(self.id)
    obj = self.read.delay(self, self.model, id)
    result = obj.get(timeout=None)
    return result

  def post_search(self, filters):
    if filters['title']:
      if filters['start_date'] and filters['end_date']:
        result = self.model.objects.filter(Q(title__icontains=filters['title']) & Q(created_at__range=(filters['start_date'], filters['end_date'])))
      elif filters['start_date'] or filters['end_date']:
        if filters['start_date']:
          result = self.model.objects.filter(Q(title__icontains=filters['title']) & Q(created_at__gt=filters['start_date']))
        elif filters['end_date']:
          result = self.model.objects.filter(Q(title__icontains=filters['title']) & Q(created_at__gt=filters['end_date']))
      else:
        result = self.model.objects.filter(Q(title__icontains=filters['title']))
    else:
      if filters['start_date'] and filters['end_date']:
        result = self.model.objects.filter(Q(created_at__range=(filters['start_date'], filters['end_date'])))
      elif filters['start_date'] or filters['end_date']:
        if filters['start_date']:
          result = self.model.objects.filter(Q(created_at__gt=filters['start_date']))
        elif filters['end_date']:
          result = self.model.objects.filter(Q(created_at__gt=filters['end_date']))
    print(result)
    return result