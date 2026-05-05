from django.urls import path
from .views import job_list, apply_job

urlpatterns = [
    path('', job_list, name='job_list'),
    path('apply/<int:job_id>/', apply_job, name='apply_job'),
]