from django.db import models
from social.models import User 
# Create your models here.

class Active_listing(models.Model):
    add_by = models.ForeignKey(User, related_name='add_by', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photo/shop/%Y/%m/%d/')
    discrption = models.TextField()
    price = models.IntegerField(default=0)
    is_exist = models.BooleanField(default=False)
    order_by = models.ManyToManyField(User, related_name='order_by')
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title}, {self.price}"
    
    
class Watchlist(models.Model):
    user = models.ForeignKey(User, related_name='watch_user', on_delete=models.CASCADE)
    active = models.ForeignKey(Active_listing, related_name='watch_shop', on_delete=models.CASCADE)