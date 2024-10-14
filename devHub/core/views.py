from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *
from .forms import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password does not exist")
    context = {}
    return render(request, 'core/login_register.html', context)

def Home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {"rooms":rooms, 'topics':topics, "room_count":room_count}
    return render(request, 'core/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {"room":room}
    return render(request, 'core/room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"form": form}
    return render(request, 'core/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method =='POST':
        if form.is_valid:
            form = RoomForm(request.POST, instance=room, )
            form.save()
            return redirect('home')
    context = {"form":form}
    return render(request, 'core/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    context= {"room":room}
    return render(request, 'core/delete.html', context)

def topics(request):
    topics = Topic.objects.all()
    context = {'topics':topics}
    return render(request, 'core/home.html', context)


