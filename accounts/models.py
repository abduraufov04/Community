from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from blog.models import Blog

class CustomUserManager(BaseUserManager):
    def create_user(self, phonenumber, password, fullname, **extra_fields):
        if not phonenumber:
            raise ValueError('The phone number must be set')
        user = self.model(phonenumber=phonenumber, fullname=fullname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phonenumber, password, fullname, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phonenumber, password, fullname, **extra_fields)



class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    fullname = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=12, unique=True)
    
    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = ['fullname']
    username = None
    objects = CustomUserManager()

    def __str__(self) -> str:
        return f"{self.fullname}"

    
    def get_all_my_blogs(self):
        return Blog.objects.filter(author = self)
    
    def get_all_blogs_20(self):
        count = 20 - len(self.get_all_my_blogs())
        return Blog.objects.exclude(author = self)[:count]