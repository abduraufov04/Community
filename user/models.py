from django.db import models

class User(models.Model):
    user = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE, related_name="my_user")
    email = models.EmailField(blank=True, null=True)
    telegram = models.CharField(max_length=30, blank=True, null=True)
    bio =  models.CharField(max_length=500, blank=True, null=True)
    department = models.ForeignKey('admins.Department', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f"{self.user.fullname}"