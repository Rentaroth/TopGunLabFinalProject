import jwt
from django.http import HttpResponse

from rest_framework import status
from rest_framework.exceptions import APIException

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
    except APIException as err:
      print(str(err))
      return HttpResponse({"error": 'Something went wrong!' }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except TypeError as err:
      print(str(err))
      return HttpResponse({"error": 'Something went wrong!' }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as err:
      print(str(err))
      return HttpResponse({"error": 'Something went wrong!' }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  return handler
