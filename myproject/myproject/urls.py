from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),
    path('', include('users.urls')),
    path('', include('posts.urls')),
    path('', include('connections.urls')),
    path('', include('notifications.urls')),
    path('', include('messaging.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)