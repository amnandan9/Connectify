from django.urls import path
from .views import signup, user_login, user_logout, profile, edit_profile, dashboard

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('dashboard/', dashboard, name='dashboard'),
]