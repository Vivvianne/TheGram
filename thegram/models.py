from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    image = models.ImageField(upload_to = "images/",null = True)
    title = models.CharField(max_length = 60, default = "")
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
