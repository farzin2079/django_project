import json
import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from persiantools.jdatetime import JalaliDate
from django.contrib import messages

from .models import User, Post, Comment, Appointment
from shop.choices import time_choices

# Create your views here.
def socialIndex(request):
    posts = Post.objects.all()
    
    times = {}
    try:
        appointment = Appointment.objects.all()
        for i in time_choices:
            if not i in appointment.time:
                times[i] = time_choices[i]
    except:
        times = time_choices
    return render(request, 'social/index.html',{
        'posts':posts,
        'times':times
    })
    
def appointment(request):
    if request.method == "POST":
        time = request.POST['time']
        day = request.POST['day']
        user = User.objects.get(username=request.user)
        today = JalaliDate.today()
        if day == 'today':
            date = today
        elif day == 'tommarow':
            date = today + datetime.timedelta(hours=24)
        elif day == 'after':
            date = today + datetime.timedelta(hours=48)
        else:
            messages.error(request, 'invalid day')
            return HttpResponseRedirect(reverse('socialIndex'))
        
        print(type(date.strftime('%Y%m%d')))
        print(type(time))
        
        try:
            Appointment.objects.get(date=date.strftime('%Y-%m-%d'), time=time)
            messages.error(request, 'this appointmnet already taked')
            return HttpResponseRedirect(reverse('socialIndex'))
        except:
            appointment = Appointment(customer=user, date=date, time=time, is_taked=True)
            appointment.save()
        return HttpResponseRedirect(reverse('accountIndex'))
        
    else:
        messages.error(request, 'invalid submit')
        return HttpResponseRedirect(reverse('socialIndex'))
        
def time_choice(request, day):
    today = JalaliDate.today()
    
    if day == 'today':
        date = today
    elif day == 'tommarow':
        date = today + datetime.timedelta(hours=24)
    elif day == 'after':
        date = today + datetime.timedelta(hours=48)
        
    appointment = Appointment.objects.filter(date=date.strftime('%H%m%d'))
    return JsonResponse(appointment)