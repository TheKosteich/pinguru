from django.db import models
from django.contrib.auth.models import AbstractUser


# Table for custom user
class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    department = models.CharField(max_length=200, verbose_name='Название структурного подразделения')
