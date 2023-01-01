from django.urls import path

from . import views

urlpatterns = [
    path('', views.accountIndex, name='accountIndex'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('delete', views.delete, name='delete'),
    path('logout', views.logout_view, name='logout'),
    path('watchlist', views.watchlist, name='watchlist'),
]
