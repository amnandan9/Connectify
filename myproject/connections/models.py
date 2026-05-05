from django.db import models
from django.contrib.auth.models import User

class Connection(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received')
    accepted = models.BooleanField(default=False)