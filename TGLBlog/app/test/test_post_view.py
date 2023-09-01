from django.http import JsonResponse
from rest_framework.test import APIClient
from django.urls import reverse
from app.services.post_service import PostService

class TestCasePostView:
  def test_post_post_method(self, mocker):
    # Gets the endpoint url
    url = reverse('posts')
    #generates an API client for testing
    client = APIClient()

    # Stubs and spies
    post_instance= mocker.spy(obj=PostService, name='__init__')
    post_creation_service_stub = mocker.stub(name='post_creation_service')

    #Return of the service function
    post_creation_service_stub.return_value = {
      "_id": "64f0f0ckwdb82df9dd986e97",
      "title": "Titulo marginadamente sensual",
      "content": "Contenido espectacular",
      "status": "active",
      "user_id": "64f0f03d1c6b47a329d1c9ad",
      "category_id": "64f0f0ababb82df9dd986e95",
      "tag_id": ["64f0f0cbabb82df9dd986e97", "64f0f0d5abb82df9dd986e98"]
    }

    #Dummy data that corresponds to return_value

    dummy_data = {
      'data': {
        "title": "Titulo marginadamente sensual",
        "content": "Contenido espectacular",
        "status": "active",
        "user_id": "64f0f03d1c6b47a329d1c9ad",
        "category_id": "64f0f0ababb82df9dd986e95",
        "tag_id": ["64f0f0cbabb82df9dd986e97", "64f0f0d5abb82df9dd986e98"]
      }
    }
   
    #Binding stub to service function
    mocker.patch('app.services.post_service.PostService.PostCreationService', post_creation_service_stub)
    mocker.patch('app.services.post_service.PostService', return_value=post_instance)

    #POST request using API client and dummy_data
    response = client.post(url, data=dummy_data, format='json')

    #Asserts
    post_creation_service_stub.assert_called_once()
    response.status_code == 200
    assert post_instance.call_count == 1
    assert isinstance(response, JsonResponse)

  def test_get_post_method(self, mocker):
    #Gets the endpoint url
    url = reverse('posts') + '/64f0f03d1c6b47a329d1c9ad'
    
    #generates an API client for testing
    client = APIClient()

    #Stub for service function
    post_instance = mocker.spy(obj=PostService, name='__init__')
    post_get_service_stub = mocker.stub(name='post_get_service_stub')

    #Return of the service function
    post_get_service_stub.return_value = {
      "_id": "64f0f0ckwdb82df9dd986e97",
      "title": "Titulo marginadamente sensual",
      "content": "Contenido espectacular",
      "status": "active",
      "user_id": "64f0f03d1c6b47a329d1c9ad",
      "category_id": "64f0f0ababb82df9dd986e95",
      "tag_id": ["64f0f0cbabb82df9dd986e97", "64f0f0d5abb82df9dd986e98"]
    }
    
    #Binding stub to service function
    mocker.patch('app.services.post_service.PostService.PostGetService', post_get_service_stub)
    mocker.patch('app.services.post_service.PostService', return_value=post_instance)

    #GET request using API client
    response = client.get(url, format='json')

    #Asserts
    assert post_instance.call_count == 1
    post_get_service_stub.assert_called_once()
    assert isinstance(response, JsonResponse)

  def test_update_post_method(self, mocker):
    #Gets the endpoint url
    url = reverse('posts') + '/64f0f03d1c6b47a329d1c9ad'
    
    #generates an API client for testing
    client = APIClient()

    #Stub for service function
    post_instance = mocker.spy(obj=PostService, name='__init__')
    post_update_service_stub = mocker.stub(name='post_update_service_stub')

    #Return of the service function
    post_update_service_stub.return_value = {
      "_id": "64f0f0ckwdb82df9dd986e97",
      "title": "Titulo marginadamente sensual",
      "content": "Contenido espectacular",
      "status": "active",
      "user_id": "64f0f03d1c6b47a329d1c9ad",
      "category_id": "64f0f0ababb82df9dd986e95",
      "tag_id": ["64f0f0cbabb82df9dd986e97", "64f0f0d5abb82df9dd986e98"]
    }
    
    #Binding stub to service function
    mocker.patch('app.services.post_service.PostService.PostUpdateService', post_update_service_stub)
    mocker.patch('app.services.post_service.PostService', return_value=post_instance)

    #Dummy data that corresponds to return_value

    dummy_data = {
      'data': {
        "title": "Titulo marginadamente sensual",
        "content": "Contenido espectacular",
        "status": "active",
        "user_id": "64f0f03d1c6b47a329d1c9ad",
        "category_id": "64f0f0ababb82df9dd986e95",
      }
    }

    #GET request using API client
    response = client.put(url, format='json', data = dummy_data)

    #Asserts
    assert post_instance.call_count == 1
    post_update_service_stub.assert_called_once()
    assert isinstance(response, JsonResponse)

  def test_get_post_method(self, mocker):
    #Gets the endpoint url
    url = reverse('posts') + '/64f0f03d1c6b47a329d1c9ad'
    
    #generates an API client for testing
    client = APIClient()

    #Stub for service function
    post_instance = mocker.spy(obj=PostService, name='__init__')
    post_delete_service_stub = mocker.stub(name='post_delete_service_stub')

    #Return of the service function
    post_delete_service_stub.return_value = 'Done!'
    
    #Binding stub to service function
    mocker.patch('app.services.post_service.PostService.PostDeleteService', post_delete_service_stub)
    mocker.patch('app.services.post_service.PostService', return_value=post_instance)

    #GET request using API client
    response = client.delete(url, format='json')

    #Asserts
    assert post_instance.call_count == 1
    post_delete_service_stub.assert_called_once()
    assert isinstance(response, JsonResponse)