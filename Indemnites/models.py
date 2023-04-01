from django.db import models


# Create your models here.
from Employe.models import Employe


class Indemnites(models.Model):
    # idIndemnite
    TYPE = (('Valeur fixe','Valeur fixe'),
            ('pourcentage sur salaire','pourcentage sur salaire'))
    intitule = models.CharField(max_length=50, null=True)
    valeur = models.FloatField(null=True, default=0)
    type = models.CharField(null=True, max_length=30, choices=TYPE)
    employe = models.ForeignKey(Employe, max_length=200, null=True, on_delete=models.SET_NULL)
