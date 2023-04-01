from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from Entreprise import views
from Entreprise.views import Connexion, Dash, Inscription, Erreur, activate, AjoutEntrepise, InfoEntreprise, modifientreprise, Finish
urlpatterns = [
    path('', Connexion, name='Login'),
    path('Dash', Dash, name='Dash'),
    path('inscrit', Inscription, name='inscrit'),
    path('Erreur', Erreur, name='Erreur'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('creerEntre', AjoutEntrepise, name='creerEntre'),
    path('infoEntre', InfoEntreprise, name='infoEntre'),
    path('ModifierEmplo', modifientreprise, name='ModifierEmplo'),
    path('EntrepriseMenu', views.EntrepriseMenu, name='EntrepriseMenu'),
    path('deco', Finish, name='deco'),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name='Entreprise/Login/password_reset.html'), name='reset_password'),
    path('reset_password_send', auth_views.PasswordResetDoneView.as_view(template_name='Entreprise/Login/password_reset_sent.html'), name='password_reset_done'),
    path('reset/(<uidb64>/<token>)', auth_views.PasswordResetConfirmView.as_view(template_name='Entreprise/Login/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='Entreprise/Login/password_reset_done.html'), name='password_reset_complete')

]
