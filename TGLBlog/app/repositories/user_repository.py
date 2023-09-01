from app.models import *
from .base_repository import BaseRepository
from app.models import Users

from celery import shared_task
from app.tasks import confirm_mail
from bson import ObjectId

import jwt
from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404
from django.forms import model_to_dict


class UserRepository(BaseRepository):
  model = Users
  def __init__(self):
    super().__init__()

  def create_and_send_confirmation_email(self, model, data):
    user_creation_task = self.create.delay(self, model, data)
    result = user_creation_task.get(timeout=None)
    if result != 'Not created':
      # confirm_mail.delay(to=data['email'], message='User was created.')
      return model_to_dict(result)
    else:
      return "User couldn't be created."
  
  @shared_task
  def user_object_obtention(self):
    obj = {}
    if self.id:
      obj = self.model.objects.get(_id=ObjectId(self.id))
    elif self.nickname:
      obj = get_object_or_404(self.model, nickname=self.nickname)
    elif self.email:
      obj = get_object_or_404(self.model, email=self.email)
    return obj

  @shared_task
  def login(self):
    obj = {}
    if self.id:
      obj = self.model.objects.get(_id=ObjectId(self.id))
    elif self.nickname:
      obj = get_object_or_404(self.model, nickname=self.nickname)
    elif self.email:
      obj = get_object_or_404(self.model, email=self.email)
    
    user_pass = model_to_dict(obj)
    
    if user_pass['password']:
      permission = check_password(self.password, user_pass['password'])
      if permission:
        del user_pass['password']
        return user_pass
    else:
      raise ValueError('Not enough credentials.')

