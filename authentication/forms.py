from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
class LoginForm(forms.Form):
    username = forms.CharField(max_length = 63, label = 'Nom dutilisateur')
    password = forms.CharField(max_length = 63, widget= forms.PasswordInput,  label = 'Mot de passe')


class SingForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'last_name','role']

