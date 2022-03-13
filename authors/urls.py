from aiohttp import request
from django.urls import path

from . import views

app_name = 'authors'
urlpatterns = [

    path('register/', views.register_view, name='register'),
    path('register/create/', views.register_created, name='create'),
  
  
]
