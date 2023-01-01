from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

    
class Post(models.Model):
    post_by = models.ForeignKey(User, related_name='post_by', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photo/social/%Y/%m/%d/')
    discription = models.TextField( blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title}"
    
class Comment(models.Model):
    comment_by = models.ForeignKey(User, related_name='comment_by', on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    post = models.ForeignKey(Post, related_name='post', on_delete=models.CASCADE, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.comment_by.username}"
    
    
class Appointment(models.Model):
    customer = models.ForeignKey(User, related_name='customer', on_delete=models.CASCADE)
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=6)
    is_taked = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer.username} in {self.date}"