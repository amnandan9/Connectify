from django.urls import include, path
from .views import connection_list, send_request, accept_request

urlpatterns = [
    path('connections/', connection_list, name='connections'),
    path('send-request/<int:user_id>/', send_request, name='send_request'),
    path('accept-request/<int:request_id>/', accept_request, name='accept_request'),
    path('', include('messaging.urls')),
]