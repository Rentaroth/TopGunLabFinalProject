from djongo.models.fields import ObjectId
from djongo import models

class Users(models.Model):
  _id = models.ObjectIdField(primary_key=True, default=ObjectId)
  name = models.CharField(max_length=20, unique=True)
  nickname = models.CharField(max_length=20, unique=True)
  password = models.CharField(max_length=40)
  email = models.EmailField(unique=True)
  verified = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now=True)

class Categories(models.Model):
  _id = models.ObjectIdField(primary_key=True, default=ObjectId)
  category = models.CharField(max_length=20)

class Tags(models.Model):
  _id = models.ObjectIdField(primary_key=True, default=ObjectId)
  tag = models.CharField(max_length=20)

class Posts(models.Model):
  _id = models.ObjectIdField(primary_key=True, default=ObjectId)
  title = models.CharField(max_length=20)
  content = models.TextField()
  status = models.CharField(max_length=8)
  user_id = models.ForeignKey(to=Users, on_delete=models.CASCADE, db_column='user_id')
  category_id = models.ForeignKey(to=Categories, on_delete=models.CASCADE, db_column='category_id')
  tag_id = models.ManyToManyField(to=Tags, db_column='tag_id')
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
  _id = models.ObjectIdField(primary_key=True, default=ObjectId)
  comment = models.TextField()
  user_id = models.ForeignKey(to=Users, on_delete=models.CASCADE, db_column='user_id')
  post_id = models.ForeignKey(to=Posts, on_delete=models.CASCADE, db_column='post_id')
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now=True)