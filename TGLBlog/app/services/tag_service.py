from app.repositories.tag_repository import TagRepository

from django.forms import model_to_dict

class TagService(TagRepository):
  def __init__(self, id=None):
    super().__init__()
    self.id = id
  
  def TagGetService(self):
    obj = self.obtain_all_tags()
    result = []
    for item in obj:
      res = model_to_dict(item)
      res.update({
        '_id': res['_id'].__str__()
      })
      result.append(res)
    return result