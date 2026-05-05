from django.urls import path
from .views import inbox, chat

urlpatterns = [
    path('inbox/', inbox, name='inbox'),
    path('chat/<int:user_id>/', chat, name='chat'),
]