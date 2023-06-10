from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

class Nota(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=60)
    corpo = models.TextField()
    data = models.DateTimeField(default=datetime.now, blank=True)
