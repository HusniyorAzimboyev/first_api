from django.db import models
from django.contrib.auth.models import User

class Journal(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    author = models.ForeignKey(User,on_delete=models.CASCADE)