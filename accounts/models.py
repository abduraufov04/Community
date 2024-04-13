from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='user_images/')
    fullname = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=12, unique=True)

    def __str__(self) -> str:
        return f"{self.fullname}"