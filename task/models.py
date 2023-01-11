from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class user(AbstractUser):
    username = None
    email = models.CharField(max_length=200, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

class image(models.Model):
    image = models.ImageField(upload_to='image/')