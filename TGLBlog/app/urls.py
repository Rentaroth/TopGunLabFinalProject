from django.urls import path
from .views import *

urlpatterns = [
  path('', index, name='index'),
  path('users', UsersView.as_view(), name='users'),
  path('users/<str:id>', UsersView.as_view(), name='users_id'),
  path('posts', PostsView.as_view(), name='posts'),
  path('posts/<str:id>', PostsView.as_view(), name='posts_id'),
  path('comments', CommentsView.as_view(), name='comments'),
  path('comments/<str:id>', CommentsView.as_view(), name='comments_id'),
]