from django.db import models


class Blog(models.Model):
    CHOICE_BLOG_TYPE = (
        ('news', 'Yangiliklar'),
        ('blog', 'Blog'),
        ('info', 'Malumotnoma'),
    )
    img = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    title = models.CharField(max_length = 250)
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    type = models.CharField(max_length = 30, choices=CHOICE_BLOG_TYPE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.title}"
    

class Images(models.Model):
    upload = models.ImageField(upload_to='blog_images/')
    blog = models.ForeignKey(Blog, on_delete = models.SET_NULL, blank=True, null=True)
    
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete = models.SET_NULL, blank=True, null=True)
    body = models.TextField()
    author = models.ForeignKey('accounts.CustomUSer', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return f"{self.author.fullname}"