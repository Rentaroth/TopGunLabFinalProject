from app.serializers import *
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.types import OpenApiTypes

POST_METHOD_USER = {
    "summary": "Create a new user entry",
    "description": "This method creates a new user database entry",
    "request": UserSerializer,
    "responses": {201: UserSerializer()}
}

GET_METHOD_USER = {
    "summary": "Obtain a user entry",
    "description": "This method obtains user data from a database entry",
    "responses": {201: UserSerializer()}
}

PUT_METHOD_USER = {
    "summary": "Modify a user entry",
    "description": "This method modifies user data from a database entry",
    "responses": {201: UserSerializer()}
}

DELETE_METHOD_USER = {
    "summary": "Delete a user entry",
    "description": "This method delete user data from a database entry",
    "responses": {201: UserSerializer()}
}
##
GET_METHOD_TAGS = {
    "summary": "Obtain all tags entries",
    "description": "This method obtains all tag entries from database",
    "responses": {201: TagsSerializer()}
}
##
POST_METHOD_POSTS = {
    "summary": "Create a new post",
    "description": "This method allous user to write a post and store it in database to publish",
    "request": PostSerializer,
    "responses": {201: PostSerializer()}
}

GET_METHOD_POSTS = {
    "summary": "Obtain a post",
    "description": "This method takes a post from database",
    "responses": {201: PostSerializer()}
}

PUT_METHOD_POSTS = {
    "summary": "Modify a post",
    "description": "This method modifies a post in database",
    "responses": {201: PostSerializer()}
}

DELETE_METHOD_POSTS = {
    "summary": "Delete a post",
    "description": "This method delete a post in database",
    "responses": {201: PostSerializer()}
}

###

POST_METHOD_COMMENTS = {
    "summary": "Create a new comment",
    "description": "This method allous user to write a comment, relates it with a post and stores it in database",
    "request": CommentSerializer,
    "responses": {201: CommentSerializer()}
}

GET_METHOD_COMMENTS = {
    "summary": "Obtain a comment",
    "description": "This method takes a comment from database",
    "responses": {201: CommentSerializer()}
}

PUT_METHOD_COMMENTS = {
    "summary": "Modify a comment",
    "description": "This method modifies a comment in database",
    "responses": {201: CommentSerializer()}
}

DELETE_METHOD_COMMENTS = {
    "summary": "Delete a comment",
    "description": "This method delete a comment in database",
    "responses": {201: CommentSerializer()}
}

###

GET_METHOD_CATEGORIES = {
    "summary": "Obtain all categories",
    "description": "This method takes all categories from database",
    "responses": {201: CategorySerializer()}
}

###

POST_METHOD_LIKES = {
    "summary": "Like a post",
    "description": "This method allous user to mark a post with a like snippet",
    "request": PostsLikesSerializer,
    "responses": {201: PostsLikesSerializer()}
}

###

POST_METHOD_LOGIN = {
    "summary": "Create a new comment",
    "description": "This method allous user to write a comment, relates it with a post and stores it in database",
    "request": LoginSerializer,
    "responses": {201: LoginSerializer()}
}

###

POST_METHOD_REPOSTS = {
    "summary": "Publish an existent post",
    "description": "Allows user to publish an existent post referencing its owner",
    "request": RepostSerializer,
    "responses": {201: RepostSerializer()}
}

###

POST_METHOD_SEARCHBAR = {
    "summary": "Create a new user entry",
    "description": "This method creates a new user database entry",
    "parameters": [
      OpenApiParameter(
        name='search_title',
        type=OpenApiTypes.STR,
        description='Sentence with keywords included in post title'
      ),
      OpenApiParameter(
        name='search_start_date',
        type=OpenApiTypes.STR,
        description='Start date to search from when posts were created'
      ),
      OpenApiParameter(
        name='search_end_date',
        type=OpenApiTypes.STR,
        description='Final date to search from when posts were created'
      ),
    ]
}