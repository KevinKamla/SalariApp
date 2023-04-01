from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('Sala', views.Salaire, name='salaire')

]
