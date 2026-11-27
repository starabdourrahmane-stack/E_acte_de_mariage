from django import forms
from django.contrib.auth import get_user_model
from . import models
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth.forms import UserCreationForm
class LoginForm(forms.Form):
    email = forms.EmailField(label='Adresse e-mail')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')

class SingForm(UserCreationForm):
    username = forms.CharField(label= "Nom de l'utilisateur" )
    last_name = forms.CharField( label="Prénom de l'utilisateur")
    email = forms.EmailField(label='Email')
    password1  = forms.CharField(widget= forms.PasswordInput, label="Mot de passe")
    password2  = forms.CharField(widget= forms.PasswordInput, label="Confirmer le mot de  passe")
    def clean_username(self):
        return self.cleaned_data['username']
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'last_name', 'password1', 'password2']

class UploadProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields =['profile_photo']

class MonPasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].label = "Ancien mot de passe"

        self.fields['new_password1'].label = "Nouveau mot de passe"

        self.fields['new_password2'].label = "Confirmer le nouveau mot de passe"

        self.fields['new_password1'].help_text = (
            "Votre mot de passe doit contenir au moins 8 caractères."
        )