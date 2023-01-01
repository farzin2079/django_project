from django.urls import path

from . import views

urlpatterns = [
    path('', views.socialIndex, name='socialIndex'),
    path('appointmnet', views.appointment, name='appointmnet'),
]
