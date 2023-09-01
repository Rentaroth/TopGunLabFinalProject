from django.http import HttpResponse, JsonResponse
from rest_framework.test import APIClient
from django.urls import reverse
from bson import ObjectId

from app.services.user_service import UserService

class TestCaseUserService:
  def test_post_user_method(self, mocker):
    #Gets the endpoint url
    url = reverse('users')
    
    #generates an API client for testing
    client = APIClient()

    #Stub for service function
    user_creation_service_stub = mocker.stub(name='user_creation_service_stub')
    country_filter_stub = mocker.stub(name='country_filter_stub')
    user_instance_creation = mocker.spy(obj=UserService, name='__init__')

    #Return of the service function
    result = {
      "_id": "64f0f03d1c6b47a329d1c9ad",
      "name": "Adriana",
      "nickname": "Adri",
      "password": "pbkdf2_sha256$390000$JpeSwu8CvCJFcHVhVGcIKk$D3nRuawoCkX3Xqpg3sjuALa1NmjJW/1SA/NGZnDzhrg=",
      "email": "adri@mail.io",
      "country": "CAN",
      "created_at": "2023-08-31 00:32:06.505834+00:00",
      "updated_at": "2023-08-31 00:32:06.505834+00:00"
    }
    user_creation_service_stub.return_value = result
    country_filter_stub.return_value = 'CAN'


    #Binding stub to service function
    mocker.patch('app.services.user_service.UserService.UserCreationService', user_creation_service_stub)
    mocker.patch('app.services.user_service.UserService', return_value=user_instance_creation)
    mocker.patch('app.utilities.country_data.country_filter', country_filter_stub)

    #Dummy data that corresponds to return_value
    dummy_data = {
      "data": {
        "name": "Adriana",
        "nickname": "Adri",
        "password": "asdasd",
        "country": "Canada",
        "email": "adri@mail.io"
      }
    }

    #POST request using API client and dummy_data
    response = client.post(url, data=dummy_data, format='json')

    #Asserts
    user_creation_service_stub.assert_called_once()
    response.status_code == 200
    assert user_instance_creation.call_count == 1
    assert isinstance(response, JsonResponse)

  def test_get_user_method(self, mocker):
    #Gets the endpoint url
    url = reverse('users') + '/64f0f03d1c6b47a329d1c9ad'
    
    #generates an API client for testing
    client = APIClient()

    #Stub for service function
    user_get_service_stub = mocker.stub(name='user_get_service_stub')
    user_instance_creation = mocker.spy(obj=UserService, name='__init__')

    #Return of the service function
    user_get_service_stub.return_value = {
      "_id": "64f0f03d1c6b47a329d1c9ad",
      "name": "Adriana",
      "nickname": "Adri",
      "password": "pbkdf2_sha256$390000$JpeSwu8CvCJFcHVhVGcIKk$D3nRuawoCkX3Xqpg3sjuALa1NmjJW/1SA/NGZnDzhrg=",
      "email": "adri@mail.io",
      "country": "CAN",
      "created_at": "2023-08-31 00:32:06.505834+00:00",
      "updated_at": "2023-08-31 00:32:06.505834+00:00"
    }
    
    #Binding stub to service function
    mocker.patch('app.services.user_service.UserService.UserGetService', user_get_service_stub)
    mocker.patch('app.services.user_service.UserService', return_value=user_instance_creation)

    #GET request using API client
    response = client.get(url, format='json')

    #Asserts
    assert user_instance_creation.call_count == 1
    user_get_service_stub.assert_called_once()
    assert isinstance(response, JsonResponse)
  
  def test_put_user_method(self, mocker):
    #Gets the endpoint url
    url = reverse('users') + '/64f0f03d1c6b47a329d1c9ad'
    
    #generates an API client for testing
    client = APIClient()

    #Stub for service function
    user_update_service_stub = mocker.stub(name='user_update_service_stub')
    user_instance_creation = mocker.spy(obj=UserService, name='__init__')

    #Return of the service function
    user_update_service_stub.return_value = {
      "_id": "64f0f03d1c6b47a329d1c9ad",
      "name": "Nadia",
      "nickname": "Nad",
      "password": "pbkdf2_sha256$390000$JpeSwu8CvCJFcHVhVGcIKk$D3nRuawoCkX3Xqpg3sjuALa1NmjJW/1SA/NGZnDzhrg=",
      "email": "nad@mail.io",
      "country": "CAN",
      "created_at": "2023-08-31 00:32:06.505834+00:00",
      "updated_at": "2023-08-31 00:32:06.505834+00:00"
    }

    #Binding stub to service function
    mocker.patch('app.services.user_service.UserService.UserUpdateService', user_update_service_stub)
    mocker.patch('app.services.user_service.UserService', return_value=user_instance_creation)

    #Dummy data that corresponds to return_value
    dummy_data = {
      "data": {
        "name": "Nadia",
        "nickname": "Nad",
        "email": "nad@mail.io"
      }
    }

    #PUT request using API client
    response = client.put(url, data=dummy_data, format='json')

    #Asserts
    assert user_instance_creation.call_count == 1
    user_update_service_stub.assert_called_once()
    assert isinstance(response, JsonResponse)

  def test_delete_user_method(self, mocker):
    #Gets the endpoint url
    url = reverse('users') + '/64f0f03d1c6b47a329d1c9ad'
    
    #generates an API client for testing
    client = APIClient()

    #Stub for service function
    user_update_service_stub = mocker.stub(name='user_delete_service_stub')
    user_instance_creation = mocker.spy(obj=UserService, name='__init__')

    #Return of the service function
    user_update_service_stub.return_value = {
      "_id": "64f0f03d1c6b47a329d1c9ad",
      "name": "Nadia",
      "nickname": "Nad",
      "password": "pbkdf2_sha256$390000$JpeSwu8CvCJFcHVhVGcIKk$D3nRuawoCkX3Xqpg3sjuALa1NmjJW/1SA/NGZnDzhrg=",
      "email": "nad@mail.io",
      "country": "CAN",
      "created_at": "2023-08-31 00:32:06.505834+00:00",
      "updated_at": "2023-08-31 00:32:06.505834+00:00"
    }

    #Binding stub to service function
    mocker.patch('app.services.user_service.UserService.UserUpdateService', user_update_service_stub)
    mocker.patch('app.services.user_service.UserService', return_value=user_instance_creation)

    #Dummy data that corresponds to return_value
    dummy_data = {
      "data": {
        "name": "Nadia",
        "nickname": "Nad",
        "email": "nad@mail.io"
      }
    }

    #PUT request using API client
    response = client.put(url, data=dummy_data, format='json')

    #Asserts
    assert user_instance_creation.call_count == 1
    user_update_service_stub.assert_called_once()
    assert isinstance(response, JsonResponse)