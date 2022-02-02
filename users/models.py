import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from django_jalali.db.models import jDateTimeField


def split_basename(file):
    basename = os.path.basename(file)
    name, ext = os.path.splitext(basename)
    return name, ext


def upload_avatar_path(file, instance):
    name, ext = split_basename(file)
    path = f'users/avatars/{instance.username}/{instance.username}{ext}'
    return path


class User(AbstractUser):
    username = models.CharField(max_length=70, unique=True, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    avatar = models.ImageField(upload_to=upload_avatar_path, blank=True, null=True)
    date_joined = jDateTimeField(auto_now_add=True)
    last_login = jDateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.username
