from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import Active_listing, Watchlist
from social.models import User
from .choices import price_choices
# Create your views here.

def shopIndex(request):
    active_listing = Active_listing.objects.all()
    
    user = User.objects.get(username=request.user)  
    watchlist = Watchlist.objects.all()
    return  render(request, 'shop/index.html',{
        'listings':active_listing,
        'price_choices':price_choices,
        'watchlist':watchlist
    })
    
def search(request):
    active_listing = Active_listing.objects.all()
    if 'price' in request.GET :
        price = request.GET['price']
        if price:
            active_listing = active_listing.filter(price__lte=price)
            
    return  render(request, 'shop/search.html',{
        'listings':active_listing,
        'price_choices':price_choices,
        'values':request.GET
    })

def watchlist(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        listing_id = request.POST['listing_id']
        listing = Active_listing.objects.get(pk=listing_id)
        try:
            # Delete if added
            watchlist = Watchlist.objects.get(user=user , active=listing)
            watchlist.delete()
            messages.warning(request, 'delete from watchlist')
        except:
            # Add new watchlist
            watchlist = Watchlist(user=user ,active=listing)
            watchlist.save()
            messages.warning(request, 'add to watchlist')
          
    return HttpResponseRedirect(reverse('shopIndex'))