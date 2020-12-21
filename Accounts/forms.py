from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from Stagaire.models import Stagaire




class registerForm(UserCreationForm):
     email = forms.EmailField(max_length=254,required=True)

     class Meta:
         model = User
         fields=(
             'username',
             'first_name',
             'last_name',
             'email',
             'password1',
             'password2'
             )
     def save(self,commit=True):
        user=super(registerForm,self).save(commit=False)
        user.first_name= self.cleaned_data.get('first_name')
        user.last_name= self.cleaned_data.get('last_name')
        user.email= self.cleaned_data.get('email')

        if commit:
            user.save()

        return user



class finishInfo(forms.ModelForm):
    class Meta:
        model = Stagaire
        fields=(
            'nom',
            'prenom',
            'dateDeNaissance',
            'telephone',
            'mail',
            'Sexe',
            'filiere',
            'niveau',
        )


class updateUserInfo(UserChangeForm):
    class Meta:
        model =User
        fields=(
            'first_name',
            'last_name',
            'email',
            
        )
    
    