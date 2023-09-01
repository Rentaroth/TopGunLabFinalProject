from app.models import *
from .base_repository import BaseRepository
from app.models import Comments

class CommentRepository(BaseRepository):
  model = Comments
  def __init__(self):
    super().__init__()