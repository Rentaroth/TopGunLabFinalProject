from django.utils import timezone
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=20)
  nickname = serializers.CharField(max_length=20)
  password = serializers.CharField(min_length=8)
  email = serializers.EmailField()
  created_at = serializers.DateTimeField(default=timezone.now().__str__())
  updated_at = serializers.DateTimeField(default=timezone.now().__str__())

  class Meta:
    model = Users
    fields = '__all__'

class PostSerializer(serializers.Serializer):
  title = serializers.CharField(max_length=200)
  content = serializers.CharField()
  status = serializers.CharField(max_length=8)
  user_id = serializers.CharField(max_length=24)
  #category_id = serializers.CharField(max_length=24)
  created_at = serializers.DateTimeField(default=timezone.now().__str__())
  updated_at = serializers.DateTimeField(default=timezone.now().__str__())
  
  class Meta:
    model = Posts
    fields = '__all__'

class CommentSerializer(serializers.Serializer):
  comment = serializers.CharField()
  user_id = serializers.CharField(max_length=24)
  post_id = serializers.CharField(max_length=24)
  created_at = serializers.DateTimeField(default=timezone.now().__str__())

  class Meta:
    model = Comments
    fields = '__all__'