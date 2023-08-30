from app.models import *
from .base_repository import BaseRepository
from app.models import Categories
from bson import ObjectId

class CategoryRepository(BaseRepository):
  model = Categories
  def __init__(self):
    super().__init__()

  def obtain_one_category(self):
    result = self.read.delay(self, self.model, ObjectId(self.id))
    res = result.get(timeout=None)
    return res

  def obtain_all_categories(self):
    result = self.model.objects.all()
    return result