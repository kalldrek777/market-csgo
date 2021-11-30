from django.contrib import admin
from django.urls import path
from weapons.views import *
from weapons.views import knife, weapons

urlpatterns = [
    path('knifes/', knife, name='knife_page'),
    path('weapons/', weapons, name='weap_page')
]