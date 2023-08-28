import time,requests
from django.core.cache import cache
from celery import shared_task

url = 'https://restcountries.com/v3.1/all'

@shared_task
def periodic_country_api_call():
  country_catalog.delay()

@shared_task
def country_catalog():
  data = requests.get(url)
  result = data.json()
  setting_countries_in_cache(result)

def setting_countries_in_cache(data):
  return cache.set('countries', data, timeout=3600)

if __name__ == '__main__':
  periodic_country_api_call.apply_async()