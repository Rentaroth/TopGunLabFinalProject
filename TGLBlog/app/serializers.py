from django.utils import timezone
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=20)
  nickname = serializers.CharField(max_length=20)
  password = serializers.CharField(min_length=8)
  email = serializers.EmailField()
  country = serializers.CharField()
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
  category_id = serializers.CharField(max_length=24)
  created_at = serializers.DateTimeField(default=timezone.now().__str__())
  updated_at = serializers.DateTimeField(default=timezone.now().__str__())
  
  class Meta:
    model = Posts
    fields = '__all__'

class RepostSerializer(serializers.Serializer):
  user_id = serializers.CharField(max_length=24)
  post_id = serializers.CharField(max_length=24)

  class Meta:
    model = Reposts
    fields = '__all__'

class PostsLikesSerializer(serializers.Serializer):
  user_id = serializers.CharField(max_length=24)
  post_id = serializers.CharField(max_length=24)

  class Meta:
    model = PostsLikes
    fields = '__all__'

class CommentSerializer(serializers.Serializer):
  comment = serializers.CharField()
  user_id = serializers.CharField(max_length=24)
  post_id = serializers.CharField(max_length=24)
  created_at = serializers.DateTimeField(default=timezone.now().__str__())

  class Meta:
    model = Comments
    fields = '__all__'

class CategorySerializer(serializers.Serializer):
  category = serializers.CharField()

  class Meta:
    model = Categories
    fields = '__all__'

class TagsSerializer(serializers.Serializer):
  category = serializers.CharField()

  class Meta:
    model = Tags
    fields = '__all__'

class LoginSerializer(serializers.Serializer):
  nickname = serializers.CharField(max_length=20, required=False)
  password = serializers.CharField(min_length=8)
  email = serializers.EmailField(required=False)

  class Meta:
    model = Users
    fields = '__all__'