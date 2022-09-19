from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/avatar/%Y/%m')


class Category(models.Model):
    name = models.CharField(max_length=50)


class News(models.Model):
    title = models.CharField(max_length=255, null=True)
    descriptions = models.CharField(max_length=500, null=True)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/news/%Y/%m')
    author = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
