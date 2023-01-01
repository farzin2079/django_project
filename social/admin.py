from django.contrib import admin

# Register your models here.
from .models import User, Post, Comment, Appointment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','post_by', 'timestamp')
    list_display_links = ('id' , 'title')
    search_fields = ('title', 'id')
    list_per_page = 20
    
class AppointmnetAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date', 'time')
    list_display_links = ('id', 'customer')
    search_fields = ('cutomer', 'date', 'time')
    list_per_page = 20
    
    
admin.site.register(User)
admin.site.register(Post, PostAdmin)
admin.site.register(Appointment, AppointmnetAdmin)