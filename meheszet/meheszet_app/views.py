from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import View

from .models import AddUser, Breeding, Beehive
from django.contrib import messages

import hashlib as hl


# Create your views here.


###AddUser function###
def index(request):
    request.session.modified = True
    if 'username' in request.session:
        del request.session['username']
    return render(request, 'meheszet_app/index.html', {})


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


def login(request, **kwargs):
    finduser = False
    findpass = False
    userdata = AddUser.objects.all().values()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        for i in range(len(userdata)):
            getUserIndex = -1

            if userdata[i]['username'] == username:
                finduser = True
                getUserIndex = i
                if userdata[getUserIndex]['password'] == hl.sha256(password.encode('utf-8')).hexdigest():
                    findpass = True
                if finduser == True and findpass == True:
                    SS = request.session['username'] = username
                    break

        if finduser == False:
            messages.error(request, "Hibás felhasználónév vagy jelszó!")
        elif findpass == False:
            messages.error(request, "Hibás felhasználónév vagy jelszó!")
        elif finduser == True and findpass == True and request.session['username'] != "":
            return HttpResponseRedirect(reverse('loggedIn'))
        elif request.session['username'] == "":
            return render(request, 'meheszet_app/index.html')

    return render(request, 'meheszet_app/login.html')


def loggedIn(request):
    var = request.session.get('username')
    if var == "":
        return redirect('index')
    if var in request.session:
        del request.session['username']
        return redirect('index')
    elif 'username' not in request.session:
        # del request.session['username']
        return redirect('index')
    elif request.session['username'] != "":
        return render(request, 'meheszet_app/loggedIn.html', {'userdata': var})


def logOut():
    return redirect('index')


###Breedings function###
def addNewBreeding(request):
    if request.method == 'POST':
        username = request.session.get('username')
        breedingcode = request.POST['code']

        print(username, " ", breedingcode)

        new_code = Breeding(username=username, breedingcode=breedingcode)
        new_code.save()
    return JsonResponse({"addBreeding":"OK" })


def getUserBreeding(request):
    if request.method == 'GET':
        breeading = Breeding.objects.all()
        values = list(breeading.values())
        filtered = []

        for i in range(0, len(values)):
            if dict(values.__getitem__(i)).get('username') == request.session['username']:
                filtered.append(dict(zip(list(values.__getitem__(i)), dict(values.__getitem__(i)).values())))
        return JsonResponse({"breeding": filtered})

def breedingDelete(request):
    breedingcode=request.GET.get('breedingcode','')
    print(breedingcode)

    breeding_delete = Breeding.objects.filter(breedingcode=breedingcode)
    for code in breeding_delete:
        breeding_delete.delete()

    beehive_delete =Beehive.objects.filter(breedingcode=breedingcode)
    for code in beehive_delete:
        beehive_delete.delete()

    return redirect('breeding')


###Beehive function###
def getUserBeehivesByBreedingCode(request):
    if request.method == 'GET':
        beehives = Beehive.objects.all()
        values = list(beehives.values())
        filtered = []
        # print(request.GET)
        for i in range(0, len(values)):
            if dict(values.__getitem__(i)).get('breedingcode') == request.GET.get('code'):
                filtered.append(dict(zip(list(values.__getitem__(i)), dict(values.__getitem__(i)).values())))
        # render(request, 'meheszet_app/loggedIn.html', {'breedingnumber': request.GET.get('code')})
    return JsonResponse({"beehives": filtered})


def deleteBeehivesByCode(request):
    breedingcode = request.GET.get('breedingcode', '')
    beehivenumber = request.GET.get('number','')

    beehive_delete = Beehive.objects.all().filter(breedingcode=breedingcode,beehivenumber=beehivenumber)
    for code in beehive_delete:
        beehive_delete.delete()

    return redirect('beehives')


def addBeehives(request):
    print(request.session.keys())
    if request.method == 'POST':
        hivenumber = request.POST['hivenumber']
        beecolor = request.POST['color']
        queenbeeyear = request.POST['queenbeeyear']
        strength = request.POST['strength']
        hiveType = request.POST['hiveType']
        breedingcode = request.session['selectedBreedingCode']
        print("Breedingcode", breedingcode)

        new_beehive = Beehive(breedingcode=breedingcode, beehivenumber=hivenumber, queenbeeyear=queenbeeyear,
                              queenbeecolor=beecolor, beehivestrength=strength, typeofhive=hiveType)
        new_beehive.save()
        # del request.session['selectedBreedingCode']
        # return redirect('loggedIn')
        # return HttpResponse(render(request,'meheszet_app/beehives.html'))
        return HttpResponse("Hello")


def getBeehivePage(request):
    print("OPEN ADD BEEHIVE")
    selectedBreedingCode = request.GET.get('code', '')
    print("Breedingcode1", request.GET.get('code', ''))
    request.session['selectedBreedingCode'] = selectedBreedingCode
    print(request.session.keys())
    return render(request, 'meheszet_app/addBeehive.html', {"selectedBreedingCode": selectedBreedingCode})


def getBackBeehivePage(request):
    return render(request, 'meheszet_app/beehives.html')
