from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext

from .models import AddUser
from django.contrib import messages

import hashlib as hl


# Create your views here.

def index(request):
    return render(request, 'meheszet_app/index.html')


def registration(request):
    finduser = False
    findemail = False
    userdata = AddUser.objects.all().values()
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['re-password']
        email = request.POST['email']

        for i in range(len(userdata)):
            if userdata[i]['username'] == username:
                finduser = True
            elif userdata[i]['email'] == email:
                findemail = True

        if len(request.POST.getlist('firstname')) == "":
            messages.error(request, "Add meg a vezetéknevet!")
        elif len(request.POST.getlist('lastname')) == "":
            messages.error(request, "Add meg a keresztnevet!")
        elif len(request.POST.getlist('username')) == "":
            messages.error(request, "Add meg a felhasználó nevet!")
        elif finduser == True:
            messages.error(request, "Ez a felhasználó név már létezik!")
        elif len(request.POST.getlist('email')) == "":
            messages.error(request, "Add meg az email címet!")
        elif findemail == True:
            messages.error(request, "Ezzel az email címmel már regisztráltak!")
        elif len(request.POST.getlist('password')) == "":
            messages.error(request, "Add meg a jelszót!!")
        elif len(request.POST.getlist('password')) != len(request.POST.getlist('re-password')):
            messages.error(request, "A két jelszó nem egyezik meg!!")
        else:
            new_user = AddUser(firstname=firstname, lastname=lastname, username=username,
                               password=hl.sha256(password.encode('utf-8')).hexdigest(),
                               email=email)
            new_user.save()
            return redirect('index')

    return render(request, 'meheszet_app/registration.html', {})


def createUser():
    return HttpResponse("Új felhasználó létrehozva!")


def login(request):
    finduser = False
    findpass = False
    userdata = AddUser.objects.all().values()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        for i in range(len(userdata)):
            if userdata[i]['username'] == username:
                finduser = True
            elif userdata[i]['password'] == hl.sha256(password.encode('utf-8')).hexdigest():
                findpass = True

        if len(request.POST.getlist('username')) == "":
            messages.error(request, "Add meg a felhasználó nevet!")
        elif finduser == False:
            messages.error(request, "Hibás felhasználónév vagy jelszó!")
        elif len(request.POST.getlist('password')) == "":
            messages.error(request, "Add meg a jelszót!")
        elif findpass == False:
            messages.error(request, "Hibás felhasználónév vagy jelszó!")
        elif finduser == True and findpass == True:
            return redirect('loggedIn')

    return render(request, 'meheszet_app/login.html')


def loggedIn(request):
    return render(request, 'meheszet_app/loggedIn.html')
