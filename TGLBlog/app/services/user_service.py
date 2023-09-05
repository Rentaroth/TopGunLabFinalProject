from app.serializers import UserSerializer
from app.repositories.user_repository import UserRepository
from app.utilities.country_data import country_filter

from django.utils import timezone
from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.forms import model_to_dict
from bson import ObjectId

class UserService(UserRepository):
  serializer = UserSerializer
  def __init__(self, id=None, name=None, nickname=None, password=None, country=None, email=None):
    super().__init__()
    self.self_instance = self
    self.id = id
    self.name = name
    self.nickname = nickname
    self.password = password
    self.country = country
    self.email = email

  def UserCreationService(self):
    created = timezone.now()
    updated = timezone.now()
    data = {
      'name': self.name,
      'nickname': self.nickname,
      'password': make_password(self.password),
      'email': self.email,
      'country': self.country,
      'verified': False,
      'created_at': created.__str__(),
      'updated_at': updated.__str__(),
    }
    validator = self.serializer(data=data)
    if validator.is_valid():
      validated = dict(validator.validated_data)
      country = country_filter(validated['country'])
      validated.update({
        'country': country,
        'created_at': validator.validated_data['created_at'].__str__(),
        'updated_at': validator.validated_data['updated_at'].__str__(),
      })
      result = self.create_and_send_confirmation_email(self.model, validated)
      if type(result) != type('str'):
        result.update({
          '_id': result['_id'].__str__()
        })
      return result
    else:
      print(validator.error_messages)
      raise ValueError("Data can't be validated!")
    
  def UserGetService(self):
    id = ObjectId(self.id)
    obj = self.read.delay(self, self.model, id)
    result = obj.get(timeout=None)
    res = model_to_dict(result)
    res['_id'] = str(res['_id'])
    return res

  def UserUpdateService(self):
    id = ObjectId(self.id)
    data = {
      'name': self.name,
      'nickname': self.nickname,
      'password': self.password,
      'email': self.email,
      'updated_at': timezone.now().__str__(),
    }
    data = {i: j for i, j in data.items() if j is not None}
    validator = self.serializer(data=data, partial=True)
    if validator.is_valid():
      validated = dict(validator.validated_data)
      validated.update({
        'updated_at': validator.validated_data['updated_at'].__str__(),
      })
    else:
      print(validator.error_messages)
      raise ValueError("Data can't be validated!")
    
    try:
      obj = self.update.delay(self, self.model, data, id)
      result = obj.get(timeout=None)
      res = model_to_dict(result)
      res['_id'] = str(res['_id'])
      return res
    except Exception as error:
      print(error)
      return {'error': 'User not found.'}

  def UserDeleteService(self):
    id = ObjectId(self.id)
    obj = self.delete.delay(self, self.model, id)
    result = obj.get(timeout=None)
    return result