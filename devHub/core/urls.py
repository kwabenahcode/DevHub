from django.urls import path
from .views import *


urlpatterns = [
    path('home/', Home, name='home'),
    path('room/<int:pk>/', room, name='room'),
    path('create-room/', createRoom, name='create-room')
]