from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('login/',views.login,name='login'),
    path('loggedIn/', views.loggedIn,name='loggedIn'),
    path('', views.logOut,name='logOut'),
    path('loggedIn/breedings', views.getUserBreeding, name='breeding')

]