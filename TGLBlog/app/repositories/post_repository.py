from app.models import *
from .base_repository import BaseRepository
from app.models import Posts, Tags
from django.db.models import Q
from django.forms import model_to_dict
from celery import shared_task

class PostRepository(BaseRepository):
  model = Posts
  def __init__(self):
    super().__init__()

  def post_object_obtention(self):
    id = ObjectId(self.id)
    obj = self.read.delay(self, self.model, id)
    result = obj.get(timeout=None)
    return result

  @shared_task
  def tag_insert(self, validated):
    instance = self.model.objects.create(**validated)
    for tag in self.tag_id:
        tag_obj = ObjectId(tag)
        instance.tag_id.add(tag_obj)
    instance.save()
    return instance

  def post_search(self, filters):
    result = self.model.objects.filter(Q(title__icontains=filters['title']) & Q(created_at__range=(filters['start_date'], filters['end_date'])))
    return result