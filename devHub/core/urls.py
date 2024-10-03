from django.urls import path
from .views import *


urlpatterns = [
    path('home/<int:pk>', Home, name='home'),
    path('room/', room, name='room'),
]