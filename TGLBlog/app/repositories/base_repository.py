from app.models import *
from celery import shared_task
from django.shortcuts import get_object_or_404

class BaseRepository:
  @shared_task
  def create(self, model, data):
    try:
      instance = model.objects.create(**data)
      instance.save()
      return instance
    except Exception as error:
      print(error)
      return 'Not created'

  @shared_task
  def read(self, model, id):
    try:
      result = get_object_or_404(model, _id = id)
      return result
    except Exception as error:
      print(error)
      return {'error': error}
  

  @shared_task
  def update(self, model, data, id):
    try:
      instance = get_object_or_404(model, _id=id)
      for key, value in data.items():
        setattr(instance, key, value)
      instance.save()
      return instance
    except Exception as err:
      print(err)
      return {'error': err}

  @shared_task
  def delete(self, model, id):
    try:
      instance = get_object_or_404(model, _id=id)
      instance.delete()
      return 'Deleted!'
    except Exception as err:
      print(err)
      return 'Not deleted.'