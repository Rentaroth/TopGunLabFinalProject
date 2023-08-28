from django.urls import path
from .views import *

urlpatterns = [
  path('login', LoginView.as_view(), name='login'),
  path('users', UsersView.as_view(), name='users'),
  path('users/<str:id>', UsersView.as_view(), name='users_id'),
  path('posts', PostsView.as_view(), name='posts'),
  path('posts/<str:id>', PostsView.as_view(), name='posts_id'),
  path('comments', CommentsView.as_view(), name='comments'),
  path('comments/<str:id>', CommentsView.as_view(), name='comments_id'),
  path('searchbar', SearchView.as_view(), name='searchbar'),
  path('categories', CategoriesView.as_view(), name='categories'),
  path('tags', TagsView.as_view(), name='tags'),
]