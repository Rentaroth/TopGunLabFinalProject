from django.http import HttpResponse, JsonResponse
from django.db.utils import DatabaseError
from .services.user_service import UserService
from .services.post_service import PostService
from .services.comment_service import CommentService
from rest_framework.views import APIView
from .models import *
from .serializers import *
import json

class UsersView(APIView):
  def post(self, request):
    data = request.data['data']
    
    try:
      service = UserService(**data)
      result = service.UserCreationService()
      return JsonResponse({'body': result})
    except DatabaseError as error:
      print(error)
      return JsonResponse({'error': error})

  def get(self, request, id):
    try:
      service = UserService(id = id)
      result = service.UserGetService()             
      return JsonResponse({'body': result})
    except DatabaseError as error:
      print(error)
      return JsonResponse({'error': error})

  def put(self, request, id):
    data = request.data['data']
    data['id'] = id
    try:
      service = UserService(**data)
      result = service.UserUpdateService()
      return JsonResponse({'body': result})
    except DatabaseError as error:
      print(error)
      return JsonResponse({'error': error})

  def delete(self, request, id):
    try:
      service = UserService(id=id)
      result = service.UserDeleteService()
      return JsonResponse({'body': result})
    except DatabaseError as error:
      print(error)
      return JsonResponse({'error': error})

class PostsView(APIView):
  def post(self, request):
    data = request.data['data']
    try:
      service = PostService(**data)
      result = service.PostCreationService()
      return JsonResponse({'body': result})
    except DatabaseError as error:
      print(error)
      return JsonResponse({'error': error})

  def get(self, request, id):
    try:
      service = PostService(id = id)
      result = service.PostGetService()
      return JsonResponse({'body': result})
    except DatabaseError as error:
      print(error)
      return JsonResponse({'error': error})

  def put(self, request, id):
    data = request.data['data']
    data['id'] = id
    try:
      service = PostService(**data)
      result = service.PostUpdateService()
      return JsonResponse({'body': result})
    except DatabaseError as error:
      print(error)
      return JsonResponse({'error': error})

  def delete(self, request, id):
    try:
      service = PostService(id=id)
      result = service.PostDeleteService()
      return JsonResponse({'body': result})
    except DatabaseError as error:
      print(error)
      return JsonResponse({'error': error})

class CommentsView(APIView):
  def post(self, request):
    data = request.data['data']
    try:
      service = CommentService(**data)
      result = service.CommentCreationService()
      return JsonResponse({'body': result})
    except DatabaseError as error:
      print(error)
      return JsonResponse({'error': error})

  def get(self, request, id):
    try:
      service = CommentService(id = id)
      result = service.CommentGetService()
      return JsonResponse({'body': result})
    except DatabaseError as error:
      print(error)
      return JsonResponse({'error': error})

  def put(self, request, id):
    data = request.data['data']
    data['id'] = id
    try:
      service = CommentService(**data)
      result = service.CommentUpdateService()
      return JsonResponse({'body': result})
    except DatabaseError as error:
      print(error)
      return JsonResponse({'error': error})

  def delete(self, request, id):
    try:
      service = CommentService(id=id)
      result = service.CommentDeleteService()
      return JsonResponse({'body': result})
    except DatabaseError as error:
      print(error)
      return JsonResponse({'error': error})

def index(request):
  return HttpResponse('Hello world!')
