from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class Post(models.Model):
    image = models.ImageField(upload_to = "images/",null = True)
    title = models.CharField(max_length = 60, default = "")
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # likes = models.ForeignKey(User, on_delete=models.CASCADE)
    # comments = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def save_image(self):
        self.save()
    
    @classmethod
    def search_by_description(cls,search_term):
        news = cls.objects.filter(description__icontains=search_term)
        return news
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    def save(self):
        super().save()
        
        img = Image.open(self.image.path)
            
        if img.height > 400 or img.width > 400:
            output_size =(400, 400)
            img.thumbnail(output_size)
            image.save(self.image.path)
            
        
# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     comment= models.TextField( blank=True)
    
#     def __str__(self):
#         return self.comment
#     def delete_comment(self):
#         self.delete()
        
#     def save_comment(self):
#     	self.save()
      





    