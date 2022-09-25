from django.db import models
from django.contrib.auth.models import AbstractUser


class Department(models.Model):
    department_name = models.CharField(max_length=4)

    def __str__(self):
        return self.department_name


class User(AbstractUser):
    account_code = models.CharField(max_length=20, null=True, blank=True)
    fullname = models.CharField(max_length=45, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    avatar = models.ImageField(upload_to='uploads/avatar/%Y/%m', null=True, blank=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class News(models.Model):
    objects = None
    title = models.CharField(max_length=255, null=True, blank=True)
    descriptions = models.CharField(max_length=500, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/news/%Y/%m')
    author = models.CharField(max_length=45, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
