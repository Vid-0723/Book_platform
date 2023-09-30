from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    # Add custom user fields if needed
    pass

# Import settings module

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    collaborators = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='collaborations')


class Section(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
