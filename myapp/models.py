from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Note(models.Model):
  title = models.CharField(min_length=5, max_length=124, blank=False, null=False)
  body = models.TextField(min_length=25, null=False, blank=False)
  user = models.ForeignKey('User', on_delete=models.CASCADE)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

class User (AbstractUser):
  username = models.CharField(max_length=150, unique=True)
  first_name = models.CharField(max_length=150)
  last_name = models.CharField(max_length=150)
  email = models.EmailField(unique=True)
  verifiedEmail = models.BooleanField(default=False)
  password = models.CharField(max_length=150)


