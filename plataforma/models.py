from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

class Task(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=60)
    data = models.DateTimeField(default=datetime.now, blank=True)
    done = models.BooleanField(default=False)
