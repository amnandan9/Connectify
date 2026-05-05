from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.CharField(max_length=200, blank=True)

    bio = models.TextField(blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)
    def __str__(self):
        return self.user.username