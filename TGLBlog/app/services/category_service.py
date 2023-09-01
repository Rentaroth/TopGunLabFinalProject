from app.repositories.category_repository import CategoryRepository
from app.models import Categories

from django.forms import model_to_dict

class CategoryService(CategoryRepository):
  model = Categories
  def __init__(self, id=None):
    super().__init__()
    self.self_instance = self
    self.id = id

  def CategoryGetService(self):
    obj = self.obtain_all_categories()
    result = []
    for item in obj:
      res = model_to_dict(item)
      res.update({
        '_id': res['_id'].__str__()
      })
      result.append(res)
    return result