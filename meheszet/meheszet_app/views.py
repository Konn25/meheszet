from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import AddUser

from django.contrib import messages

import hashlib as hl


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

        if len(request.POST.getlist('firstname')) == "":
            messages.error(request, "Add meg a vezetéknevet!")
        elif len(request.POST.getlist('lastname')) == "":
            messages.error(request, "Add meg a keresztnevet!")
        elif len(request.POST.getlist('username')) == "":
            messages.error(request, "Add meg a felhasználó nevet!")
        elif len(request.POST.getlist('email')) == "":
            messages.error(request, "Add meg az email címet!")
        elif len(request.POST.getlist('password')) == "":
            messages.error(request, "Add meg a jelszót!!")
        else:
            new_user = AddUser(firstname=firstname, lastname=lastname, username=username,
                               password=hl.sha256(password.encode('utf-8')).hexdigest(),
                               email=email)
            new_user.save()
            return redirect('index')

    return render(request, 'meheszet_app/registration.html', {})


def createUser(request):
    return HttpResponse("Új felhasználó létrehozva!")


def login(request):
    return render(request, 'meheszet_app/login.html')


def loggedIn(request):
    return render(request, 'meheszet_app/loggedIn.html')
