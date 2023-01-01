from django.contrib import admin
from .models import Active_listing, Watchlist
# Register your models here.

class Active_listingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'is_exist')
    list_display_links = ('id', 'title', 'price')
    search_fields = ('title', 'price')
    list_per_page = 20
    
admin.site.register(Active_listing, Active_listingAdmin)
admin.site.register(Watchlist)