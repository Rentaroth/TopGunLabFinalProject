from app.models import *
from .base_repository import BaseRepository
from app.models import Comments
from app.tasks import confirm_mail

class CommentRepository(BaseRepository):
  model = Comments
  def __init__(self):
    super().__init__()