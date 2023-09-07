# TGLBLOG
***
API para la creación y lectura de blogs.
***
## Table of Contents

1. [General Info](#General-Info)
2. [Technologies](#Technologies)
3. [Installation](#Installation)
4. [Docs](#Docs)

## General Info
***
Esta API, permite a los usuarios interactuar con un sistema de gestión de contenido o plataforma de blogs de manera sistemática, lo que brinda una variedad de capacidades y funcionalidades para la creación y administración de blogs.
***
## Technologies
***
Listas de tecnologías utilizadas en el proyecto:
* [Django]: Version 4.1.10
* [djangorestframework]: Version 3.14.0
* [djongo]: Version 1.3.6
* [celery]: Version 5.3.1
* [pymongo]: Version 3.13.0
* [pytest]: Version 7.4.0
***
## Installation
***
git clone https://github.com/Rentaroth/TopGunLabFinalProject.git
Con este link puedes clonar el repositorio usando git.
***
## Uso
***
* [env]: En el archivo .env puedes cambiar la variable de entorno "ENVIRONMENT" entre dev, prod y test. En el estado actual solo hay cambios para "test".
  Al establecer el entorno de test se desactivará la validación por Json Web Token lo que permitirá hacer el testing más fácilmente, si la variable no es "test" entonces la seguridad es activada.
* [start]: Instalar las dependencias listadas en el archivo requirements.txt con 'pip install', puedes iniciar el server en modo desarrollo con 'python manage.py runserver'.
  a. Windows
    - En una terminal iniciar primero celery worker con el comando "celery -A TGLBlog worker -l INFO"
    - En otra terminal iniciar luego celery beat con el comando "celery -A TGLBlog.celery:app beat -l DEBUG"
    - En otra terminal ejecutar el servidor de desarrollo de django con el comando "python manage.py runserver"

* [API]:
  - Crea un usuario haciendo una petición post en la dirección '#/users', ten en cuenta la estructura de los datos de entrada.
  - Luego podrás crear posts y comentarios. Para ello los id de las categorías y tags para los posts serían:

    a. categories:
      - 64f779cf2b84651599fb5328
      - 64f779dc2b84651599fb5329

    b. tags:
      - 64f779ac2b84651599fb5326
      - 64f779bb2b84651599fb5327
  - Por ahora es recomendable utilizar postman o insomnia.
***
## Docs
***
Este es el link de la documentación.
{host}/api/schema/swagger-ui/
***