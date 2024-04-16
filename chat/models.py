from django.db import models


class Chat(models.Model):
    message = models.CharField(max_length = 500)
    from_user = models.ForeignKey('accounts.CustomUser', on_delete = models.CASCADE, related_name="message_from")
    to_user = models.ForeignKey('accounts.CustomUser', on_delete = models.CASCADE, related_name="message_to")    
    created_at = models.DateTimeField(auto_now = True)
    
    def __str__(self) -> str:
        return f"{self.from_user} => {self.to_user}"