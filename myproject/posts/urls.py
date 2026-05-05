from django.urls import path
from .views import feed, create_post

urlpatterns = [
    path('feed/', feed, name='feed'),
    path('create-post/', create_post, name='create_post'),
]