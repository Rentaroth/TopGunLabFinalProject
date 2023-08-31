from app.models import *
from .base_repository import BaseRepository
from app.models import Categories
from bson import ObjectId
from celery import shared_task

class CategoryRepository(BaseRepository):
  model = Categories
  def __init__(self):
    super().__init__()

  @shared_task
  def obtain_one_category(self):
    result = self.model.objects.get(_id=ObjectId(self.id))
    return result

  def obtain_all_categories(self):
    result = self.model.objects.all()
    return result