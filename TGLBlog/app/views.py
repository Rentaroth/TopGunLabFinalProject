from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.conf import settings
# from .models import User
from .db_connection import db

# doc = User(name='Ligia', nickname='Liyi', password='F2vyH!z3@&yd02k{m`o[O^8J', email='liyi@mail.com', created_at=timezone.now(), updated_at=timezone.now())
# db.user.insert_one({'name': 'Antonio'})

# document = {'name': 'Ligia', 'nickname': 'Liyi', 'password': 'F2vyH!z3@&yd02k{m`o[O^8J', 'email': 'liyi@mail.com', 'created_at': timezone.now(), 'updated_at': timezone.now()}
# db.user.insert_one({'name': 'Antonio'})

# Create your views here.
def index():
  return HttpResponse('Hello world!')


async def push_one():
  pass
  # doc = Users(name='Ligia', nickname='Liyi', password='F2vyH!z3@&yd02k{m`o[O^8J', email='liyi@mail.com', created_at=timezone.now(), updated_at=timezone.now())
  # await doc.commit()

if __name__ != '__main__':
  import asyncio
  loop = asyncio.get_event_loop()
  loop.run_until_complete(push_one())