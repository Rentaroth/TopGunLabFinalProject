from app.models import *
from .base_repository import BaseRepository
from app.models import Users
from app.tasks import confirm_mail

class UserRepository(BaseRepository):
  model = Users
  def __init__(self):
    super().__init__()

  def create_and_send_confirmation_email(self, model, data):
    user_creation_task = self.create.delay(self, model, data)
    result = user_creation_task.get(timeout=None)
    if result != 'User not created':
      # confirm_mail.delay(to=data['email'], message='User was created.')
      return result
    else:
      return "User couldn't be created."
  
  def user_objcet_obtention(self):
    id = ObjectId(self.id)
    obj = self.read.delay(self, self.model, id)
    result = obj.get(timeout=None)
    return result