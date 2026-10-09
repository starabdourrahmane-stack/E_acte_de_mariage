from django import forms
from django.contrib.auth import get_user_model
from . import models
from django.contrib.auth.forms import UserCreationForm
class LoginForm(forms.Form):
    username = forms.CharField(max_length = 63, label = 'Nom dutilisateur')
    password = forms.CharField(max_length = 63, widget= forms.PasswordInput,  label = 'Mot de passe')


class SingForm(UserCreationForm):
    username = forms.CharField(label= "Nom de l'utilisateur" )
    last_name = forms.CharField( label="Prénom de l'utilisateur")
    email = forms.EmailField(label='Email')
    password1  = forms.CharField(widget= forms.PasswordInput, label="Mot de passe")
    password2  = forms.CharField(widget= forms.PasswordInput, label="Confirmer le mot de  passe")

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'last_name', 'password1', 'password2']

class UploadProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields =['profile_photo']