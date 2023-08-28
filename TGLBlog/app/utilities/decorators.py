import jwt
from django.core.cache import cache
from django.http import HttpResponse

from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework import status
from django.db import IntegrityError
from django.http import Http404

def error_handler(function):
  def handler(*args, **kwargs):
    try:
      return function(*args, **kwargs)
    except jwt.DecodeError as err:
      print(str(err))
      print("Error on decoding token")
    except jwt.ExpiredSignatureError:
      print(str(err))
      print("Expired JWT Token")
    except jwt.InvalidTokenError:
      print(str(err))
      print("Invalid JWT Token")
    except TypeError as err:
      print(str(err))
      return HttpResponse({"error": 'Something went wrong!' }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as err:
      print(str(err))
      return HttpResponse({"error": 'Something went wrong!' }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  return handler


def jwt_security_breach(function):
  @error_handler
  def security(self, request, *args, **kwargs):
    token = request.META.get('HTTP_AUTHORIZATION')
    validated = jwt.decode(token[7:], verify=True, algorithms=['HS256'])
    if validated:
      cache.set(f'token', validated, 900)
    return function(self, request, *args, **kwargs)
  return security