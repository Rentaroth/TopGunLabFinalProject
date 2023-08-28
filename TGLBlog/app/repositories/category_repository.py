from app.models import *
from .base_repository import BaseRepository
from app.models import Categories

class CategoryRepository(BaseRepository):
  model = Categories
  def __init__(self):
    super().__init__()

  def obtain_all_categories(self):
    result = self.model.objects.all()
    return result