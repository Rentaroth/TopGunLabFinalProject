from django.http import HttpResponse, JsonResponse
from django.core.cache import cache
from .services.user_service import UserService
from .services.post_service import PostService
from .services.comment_service import CommentService
from .services.category_service import CategoryService
from .services.login_service import LoginService
from .services.tag_service import TagService
from .services.repost_service import RepostService
from .services.likes_service import LikesService
from rest_framework.views import APIView
from .models import *
from .serializers import *
from drf_spectacular.utils import extend_schema
from .docs.docs import *
from rest_framework import status
from django.core.cache import cache

class LoginView(APIView):
  def post(self, request):
    try:
      credentials = request.data['data']
      service = LoginService(**credentials)
      result = service.LoginService()
      return JsonResponse({'body': result})
    except Exception as error:
      print(error)
      return JsonResponse({'body': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UsersViewNoId(APIView):
  @extend_schema(**POST_METHOD_USER)
  def post(self, request):
    try:
      data = request.data['data']
      service = UserService(**data)
      result = service.UserCreationService()
      return JsonResponse({'body': result})
    except Exception as error:
      print(error)
      return JsonResponse({'body': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UsersView(APIView):
  @extend_schema(**GET_METHOD_USER)
  def get(self, request, id):
    try:
      service = UserService(id = id)
      result = service.UserGetService()             
      return JsonResponse({'body': result})
    except Exception as error:
      print(error)
      return JsonResponse({'body': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  @extend_schema(**PUT_METHOD_USER)
  def put(self, request, id):
    try:
      data = request.data['data']
      data['id'] = id
      service = UserService(**data)
      result = service.UserUpdateService()
      return JsonResponse({'body': result})
    except Exception as error:
      print(error)
      return JsonResponse({'body': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  @extend_schema(**DELETE_METHOD_USER)
  def delete(self, request, id):
    try:
      service = UserService(id=id)
      result = service.UserDeleteService()
      return JsonResponse({'body': result})
    except Exception as error:
      print(error)
      return JsonResponse({'body': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PostViewNoId(APIView):
  @extend_schema(**POST_METHOD_POSTS)
  def post(self, request):
    try:
      data = request.data['data']
      service = PostService(**data)
      result = service.PostCreationService()
      return JsonResponse({'body': result})
    except Exception as error:
      print(error)
      return JsonResponse({'body': 'Post not created'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PostsView(APIView):
  @extend_schema(**GET_METHOD_POSTS)
  def get(self, request, id):
    try:
      service = PostService(id = id)
      result = service.PostGetService()
      return JsonResponse({'body': result})
    except Exception as error:
      print(error)
      return JsonResponse({'body': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  @extend_schema(**PUT_METHOD_POSTS)
  def put(self, request, id):
    try:
      data = request.data['data']
      data['id'] = id
      service = PostService(**data)
      result = service.PostUpdateService()
      return JsonResponse({'body': result})
    except Exception as error:
      print(error)
      return JsonResponse({'body': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  @extend_schema(**DELETE_METHOD_POSTS)
  def delete(self, request, id):
    try:
      service = PostService(id=id)
      result = service.PostDeleteService()
      return JsonResponse({'body': result})
    except Exception as error:
      print(error)
      return JsonResponse({'body': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RepostView(APIView):
  @extend_schema(**POST_METHOD_REPOSTS)
  def post(self, request, id):
    try:
      data = request.data['data']
      data.update({
        'user_id': id
      })
      service = RepostService(**data)
      result = service.RepostCreationService()
      return JsonResponse({'body': result})
    except Exception as error:
      print(error)
      return JsonResponse({'body': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LikesView(APIView):
  @extend_schema(**POST_METHOD_LIKES)
  def post(self, request, id):
    try:
      data = request.data['data']
      data.update({
        'user_id': id
      })
      service = LikesService(**data)
      result = service.LikesCreationService()
      return JsonResponse({'body': result})
    except Exception as error:
      print(error)
      return JsonResponse({'body': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CommentsViewNoId(APIView):
  @extend_schema(**POST_METHOD_COMMENTS)
  def post(self, request):
    try:
      data = request.data['data']
      service = CommentService(**data)
      result = service.CommentCreationService()
      return JsonResponse({'body': result})
    except Exception as error:
      print(error)
      return JsonResponse({'body': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CommentsView(APIView):
  @extend_schema(**GET_METHOD_COMMENTS)
  def get(self, request, id):
    try:
      service = CommentService(id = id)
      result = service.CommentGetService()
      return JsonResponse({'body': result})
    except Exception as error:
      print(error)
      return JsonResponse({'body': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  @extend_schema(**PUT_METHOD_COMMENTS)
  def put(self, request, id):
    try:
      data = request.data['data']
      data['id'] = id
      service = CommentService(**data)
      result = service.CommentUpdateService()
      return JsonResponse({'body': result})
    except Exception as error:
      print(error)
      return JsonResponse({'body': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  @extend_schema(**DELETE_METHOD_COMMENTS)
  def delete(self, request, id):
    try:
      service = CommentService(id=id)
      result = service.CommentDeleteService()
      return JsonResponse({'body': result})
    except Exception as error:
      print(error)
      return JsonResponse({'body': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CategoriesView(APIView):
  @extend_schema(**GET_METHOD_CATEGORIES)
  def get(self, request):
    try:
      service = CategoryService()
      result = service.CategoryGetService()
      return JsonResponse({'body': result})
    except Exception as error:
      print(error)
      return JsonResponse({'body': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TagsView(APIView):
  @extend_schema(**GET_METHOD_TAGS)
  def get(self, request):
    try:
      service = TagService()
      result = service.TagGetService()
      return JsonResponse({'body': result})
    except Exception as error:
      print(error)
      return JsonResponse({'body': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SearchView(APIView):
  @extend_schema(**POST_METHOD_SEARCHBAR)
  def post(self, request):
    try:
      data = request.data['data']
      service = PostService(**data)
      result = service.PostSearchService()
      return JsonResponse({'body': result})
    except Exception as error:
      print(error)
      return JsonResponse({'body': 'Internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
