import django_filters

from Stagaire.models import *

class stagaireFilter(django_filters.FilterSet):
    class Meta:
        model = Stagaire
        fields=[
            'nom',
            'prenom',
            'dateDeNaissance',
            'telephone',
            'mail',
            'filiere',
            'niveau',
        ]
