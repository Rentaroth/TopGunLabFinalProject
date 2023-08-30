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
from .utilities.decorators import error_handler
from .utilities.country_data import country_catalog

class LoginView(APIView):
  def post(self, request):
    credentials = request.data['data']
    service = LoginService(**credentials)
    result = service.LoginService()
    return JsonResponse({'body': result})

class UsersView(APIView):
  def post(self, request):
    data = request.data['data']
    service = UserService(**data)
    result = service.UserCreationService()
    return JsonResponse({'body': result})

  def get(self, request, id):
    service = UserService(id = id)
    result = service.UserGetService()             
    return JsonResponse({'body': result})

  def put(self, request, id):
    data = request.data['data']
    data['id'] = id
    service = UserService(**data)
    result = service.UserUpdateService()
    return JsonResponse({'body': result})

  def delete(self, request, id):
    service = UserService(id=id)
    result = service.UserDeleteService()
    return JsonResponse({'body': result})

class PostsView(APIView):
  def post(self, request):
    data = request.data['data']
    service = PostService(**data)
    result = service.PostCreationService()
    return JsonResponse({'body': result})

  def get(self, request, id):
    service = PostService(id = id)
    result = service.PostGetService()
    return JsonResponse({'body': result})

  def put(self, request, id):
    data = request.data['data']
    data['id'] = id
    service = PostService(**data)
    result = service.PostUpdateService()
    return JsonResponse({'body': result})

  def delete(self, request, id):
    service = PostService(id=id)
    result = service.PostDeleteService()
    return JsonResponse({'body': result})

class RepostView(APIView):
  def post(self, request, id):
    data = request.data['data']
    data.update({
      'user_id': id
    })
    service = RepostService(**data)
    result = service.RepostCreationService()
    return JsonResponse({'body': result})

class LikesView(APIView):
  def post(self, request, id):
    data = request.data['data']
    data.update({
      'user_id': id
    })
    service = LikesService(**data)
    result = service.LikesCreationService()
    return JsonResponse({'body': result})

class CommentsView(APIView):
  def post(self, request):
    data = request.data['data']
    service = CommentService(**data)
    result = service.CommentCreationService()
    return JsonResponse({'body': result})

  def get(self, request, id):
    service = CommentService(id = id)
    result = service.CommentGetService()
    return JsonResponse({'body': result})

  def put(self, request, id):
    data = request.data['data']
    data['id'] = id
    service = CommentService(**data)
    result = service.CommentUpdateService()
    return JsonResponse({'body': result})

  def delete(self, request, id):
    service = CommentService(id=id)
    result = service.CommentDeleteService()
    return JsonResponse({'body': result})

class CategoriesView(APIView):
  def get(self, request):
    service = CategoryService()
    result = service.CategoryGetService()
    return JsonResponse({'body': result})

class TagsView(APIView):
  def get(self, request):
    service = TagService()
    result = service.TagGetService()
    return JsonResponse({'body': result})

class SearchView(APIView):
  def post(self, request):
    data = request.data['data']
    service = PostService(**data)
    result = service.PostSearchService()
    return JsonResponse({'body': result})
