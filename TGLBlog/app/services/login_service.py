import jwt
from app.serializers import UserSerializer
from app.repositories.user_repository import UserRepository
from django.conf import settings
from datetime import datetime, timedelta

class LoginService(UserRepository):
  serializer = UserSerializer
  def __init__(self, id=None, nickname=None, email=None, password=None):
    super().__init__()
    self.id = id
    self.nickname = nickname
    self.email = email
    self.password = password

  def LoginService(self):
    obj = self.login.delay(self)
    inst = obj.get(timeout=None)
    inst.update({
      '_id': inst['_id'].__str__(),
      'exp': datetime.utcnow() + timedelta(hours=24)
    })
    token = jwt.encode(inst, settings.SECRET_KEY)
    return token
