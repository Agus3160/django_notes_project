from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

# Create your models here.
class Note(models.Model):
  title = models.CharField(validators=[MinLengthValidator(5)], max_length=124, blank=False, null=False)
  body = models.TextField(validators=[MinLengthValidator(25)], null=False, blank=False)
  user = models.ForeignKey('User', on_delete=models.CASCADE)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

class User (AbstractUser):
  first_name = models.CharField(max_length=150, blank=False, null=False)
  last_name = models.CharField(max_length=150, blank=False, null=False)
  email = models.EmailField(unique=True, blank=False, null=False)


