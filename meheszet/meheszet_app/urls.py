from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('loggedIn/', views.loggedIn, name='loggedIn'),
    path('', views.logOut, name='logOut'),
    path('loggedIn/breedings', views.getUserBreeding, name='breeding'),
    path('loggedIn/breedings/add', views.addNewBreeding, name='addBreeding'),
    path('loggedIn/breedings/delete/', views.breedingDelete, name='deleteBreeding'),
    path('loggedIn/breedings/beehives', views.getUserBeehivesByBreedingCode, name='beehives'),
    path('loggedIn/breedings/beehives/delete', views.deleteBeehivesByCode, name='deleteBeehive'),
    path('loggedIn/breedings/addNewBeehive/', views.getBeehivePage, name='addBeehive'),
    path('loggedIn/breedings/addNewBeehive/newHive', views.addBeehives, name='addNewBeehive'),
    path('loggedIn/breedings/beehives/', views.getBackBeehivePage, name='getBackBeehives')

]
