from django.shortcuts import render , redirect
import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


from django.contrib import messages


from social.models import User, Appointment
from shop.models import Watchlist, Active_listing


# Create your views here.
def accountIndex(request):
    user = User.objects.get(username=request.user)
    watchlists = Watchlist.objects.filter(user=user)
    listings = Active_listing.objects.all()
    
    appointments = Appointment.objects.filter(customer=user)
    return render(request , 'account/index.html',{
        'appointments':appointments,
        'watchlists':watchlists,
        'listings':listings
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            messages.success(request, 'login')
            return HttpResponseRedirect(reverse("accountIndex"))
        else:
            messages.error(request, 'invalide username and/or password')
            return redirect('login')
    else:
        return render(request, "account/login.html")

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'logout')
    return HttpResponseRedirect(reverse("socialIndex"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation: 
            # Message
            messages.error(request, 'password and confirmtion most be same')
            return redirect('register')
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            messages.error(request, 'username is already exist')
            return redirect('register')
        login(request, user)
        
        messages.success(request, 'registre successfull')
        return HttpResponseRedirect(reverse("accountIndex"))
    else:
        return render(request, "account/register.html")
    
def watchlist(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        listing_id = request.POST['listing_id']
        listing = Active_listing.objects.get(pk=listing_id)
        # Delete watchlist
        watchlist = Watchlist.objects.get(user=user , active=listing)
        watchlist.delete()
        messages.warning(request, 'object is remove from watchlist')
    return HttpResponseRedirect(reverse('accountIndex'))

def delete(request):
    if request.method == 'POST':
        appointment_id = request.POST['appointment_id']
        appointment= Appointment.objects.get(pk=appointment_id)
        appointment.delete()
        messages.success(request, 'deleted')
    else:
        messages.error(request, 'invalid submit')
    
    return redirect('accountIndex')