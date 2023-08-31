from app.models import *
from .base_repository import BaseRepository
from celery import shared_task
from app.models import Tags
from bson import ObjectId

class TagRepository(BaseRepository):
  model = Tags
  def __init__(self):
    super().__init__()

  def obtain_all_tags(self):
    result = self.model.objects.all()
    return result
  
  @shared_task
  def obtain_one_tag(self):
    result = self.model.objects.get(_id=ObjectId(self.id))
    return result
  

