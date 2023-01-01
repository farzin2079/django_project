from django.urls import path

from . import views
urlpatterns = [
    path('', views.shopIndex, name='shopIndex'),
    path('search', views.search, name='search'),
    path('watchlist', views.watchlist, name='watchlist'),
]
