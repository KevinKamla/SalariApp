from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('Entreprise.urls')),
    path('employe', include('Employe.urls')),
    path('Adresse', include('Adresse.urls')),
    path('Indemnites', include('Indemnites.urls'))
]

