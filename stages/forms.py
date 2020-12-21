from django import forms
from Stagaire.models import Stage

class addStage(forms.ModelForm):
    class Meta:
        model = Stage
        fields=(
            'DateDebut',
            'DateFin',
            'Societe',
            'Rapport',
            'stagaire',
        )



class editStage(forms.ModelForm):
    class Meta:
        model = Stage
        fields=(
            'DateDebut',
            'DateFin',
            'Societe',
            'Rapport',
            'stagaire',
        )
        
