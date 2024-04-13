from django.db import models

class SuperUser(models.Model):
    user = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE, related_name='my_superuser')

    def __str__(self) -> str:
        return f"{self.user.fullname}"