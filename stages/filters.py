import django_filters

from Stagaire.models import *

class stageFilter(django_filters.FilterSet):
    class Meta:
        model = Stage
        fields=[
            'DateDebut',
            'DateFin',
            'Societe',
            'stagaire'
        ]
