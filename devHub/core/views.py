from django.shortcuts import render, redirect
from .models import *
from .forms import *

def Home(request):
    rooms = Room.objects.all()
    context = {"rooms":rooms}
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