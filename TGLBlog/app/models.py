from umongo import Document, fields
from django.utils import timezone
from .db_connection import instance

@instance.register
class Users(Document):
  name = fields.StringField(max_length=20)
  nickname = fields.StringField(max_length=20)
  password = fields.StringField(min_length=8)
  email = fields.EmailField(allow_utf8_Users=True)
  created_at = fields.DateTimeField(default=timezone.now())
  updated_at = fields.DateTimeField(default=timezone.now())

  class Meta:
    collection_name = 'users'

@instance.register
class Categories(Document):
  category = fields.StringField()

  class Meta:
    collection_name = 'categories'

@instance.register
class Tags(Document):
  tag = fields.StringField()

  class Meta:
    collection_name = 'tags'

@instance.register
class Posts(Document):
  title = fields.StringField(max_length=20)
  content = fields.StringField()
  status = fields.StringField(max_length=8)
  Users_id = fields.ReferenceField(Users)
  category_id = fields.ReferenceField(Categories)
  created_at = fields.DateTimeField(default=timezone.now())
  updated_at = fields.DateTimeField(default=timezone.now())

  class Meta:
    collection_name = 'posts'

@instance.register
class Comments(Document):
  comment = fields.StringField()
  Users_id = fields.IntegerField()
  post_id = fields.IntegerField()
  created_at = fields.DateTimeField(default=timezone.now())

  class Meta:
    collection_name = 'comments'
