from django.urls import path
from .views import *


urlpatterns = [
    path('login/', loginPage, name='login'),
    path('home/', Home, name='home'),
    path('room/<int:pk>/', room, name='room'),
    path('create-room/', createRoom, name='create-room'),
    path('update-room/<str:pk>', updateRoom, name='update-room'),
    path('delete-room/<str:pk>', deleteRoom, name='delete-room'),
    # path('topics/', topics, name='topics')
]