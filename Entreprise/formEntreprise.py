from django.forms import ModelForm
from django import forms

from .models import Entreprise


class FormulaireEntreprise(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = [
            'formeJuridique',
            'nomEntreprise',
            'anneeCreation',
            'activite',
            'effectif',
            'capital',
            'nomDirecteur',
            'numeroContribuable',
            'formeJuridique',
            'chiffreAffaire'
        ]
