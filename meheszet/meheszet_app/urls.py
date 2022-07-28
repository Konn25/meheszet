from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('login/',views.login,name='login'),
    path('loggedIn/', views.loggedIn,name='loggedIn'),
    path('', views.logOut,name='logOut'),
    path('loggedIn/breedings', views.getUserBreeding, name='breeding'),
    path('loggedIn/breedings/add',views.addNewBreeding, name='addBreeding'),
    path('loggedIn/breedings/beehives',views.getUserBeehivesByBreedingCode, name='beehives'),
    path('loggedIn/breedings/addNewBeehive',views.addBeehives, name='addBeehive')

]