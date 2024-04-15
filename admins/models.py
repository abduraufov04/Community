from django.db import models


class Department(models.Model):
    title = models.CharField(max_length=500)
    faculty = models.CharField(max_length=500)


class Admins(models.Model):
    user = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE, related_name='my_admin')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.user.fullname}"