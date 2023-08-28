from app.models import *
from .base_repository import BaseRepository
from app.models import Tags

class TagRepository(BaseRepository):
  model = Tags
  def __init__(self):
    super().__init__()

  def obtain_all_tags(self):
    result = self.model.objects.all()
    return result