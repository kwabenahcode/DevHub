from django.urls import path
from .views import *


urlpatterns = [
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register', registerPage, name='register'),
    path('home/', Home, name='home'),
    path('room/<int:pk>/', room, name='room'),
    path('create-room/', createRoom, name='create-room'),
    path('update-room/<str:pk>', updateRoom, name='update-room'),
    path('delete-room/<str:pk>', deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>', deleteMessage, name='delete-message'),
    # path('topics/', topics, name='topics')
]