import jwt
from django.conf import settings
from django.core.cache import cache
from django.urls import reverse


class JWTAuth:
  def __init__(self, get_response):
    self.get_response = get_response
    # One-time configuration and initialization.

  def __call__(self, request):
    if settings.ENVIRONMENT == 'test':
      response = self.get_response(request)
      return response

    current_url = request.path_info
    excluded_urls = [reverse('login'), reverse('users'), reverse('swagger-ui'), reverse('redoc'), reverse('schema')]

    if current_url not in excluded_urls:
      token = request.META.get('HTTP_AUTHORIZATION') or ''
      if not token:
        raise jwt.exceptions.InvalidTokenError(f'JWT not valid: {token}')
      validated = jwt.decode(token[7:], verify=True, algorithms=['HS256'])
      if validated:
        cache.set(f'token', validated, 900)

      response = self.get_response(request)
    else:
      response = self.get_response(request)

    # Code to be executed for each request/response after
    # the view is called.

    return response