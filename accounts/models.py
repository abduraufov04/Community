from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    fullname = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=12, unique=True)
    username = None
    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = ['fullname']

    def __str__(self) -> str:
        return f"{self.fullname}"