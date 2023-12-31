from django.urls import path
from .views import *
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
  path('login', LoginView.as_view(), name='login'),
  path('users', UsersViewNoId.as_view(), name='users'),
  path('users/<str:id>', UsersView.as_view(), name='users_id'),
  path('posts', PostViewNoId.as_view(), name='posts'),
  path('posts/<str:id>', PostsView.as_view(), name='posts_id'),
  path('comments', CommentsViewNoId.as_view(), name='comments'),
  path('comments/<str:id>', CommentsView.as_view(), name='comments_id'),
  path('searchbar', SearchView.as_view(), name='searchbar'),
  path('categories', CategoriesView.as_view(), name='categories'),
  path('tags', TagsView.as_view(), name='tags'),
  path('repost/<str:id>', RepostView.as_view(), name='repost'),
  path('likes/<str:id>', LikesView.as_view(), name='likes'),
  path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
  path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
  path('schema', SpectacularAPIView.as_view(), name='schema'),
]