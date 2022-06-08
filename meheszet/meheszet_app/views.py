from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .models import AddUser

from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'meheszet_app/index.html')


def registration(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        beekepingNature = request.POST['beekepingNature']
        smallProducerRegNumber = request.POST['smallProducerRegNumber']

        if request.POST.get('firstname') is not None:
            messages.error(request, "Nem jól lett kitöltve")
        else:
            new_user = AddUser(firstname=firstname, lastname=lastname, username=username, password=password,
                               email=email,
                               beekepingNature=beekepingNature, smallProducerRegNumber=smallProducerRegNumber)
            new_user.save()
            return redirect('index')

    return render(request, 'meheszet_app/registration.html', {})


def createUser(request):
    return HttpResponse("Új felhasználó létrehozva!")


def login(request):
    return render(request, 'meheszet_app/login.html')


def loggedIn(request):
    return render(request, 'meheszet_app/loggedIn.html')
