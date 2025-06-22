from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_collector = models.BooleanField(default=False, verbose_name='هل أنت مشتري؟')
    phone_number = models.CharField(max_length=10, unique=True)
