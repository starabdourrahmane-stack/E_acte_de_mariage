from django.shortcuts import render, redirect
from django.conf import settings
from authentication import forms
from django.contrib.auth import login, authenticate, logout# import des fonctions login et authenticate
from django.core.exceptions import ValidationError

# Create your views here.

def logout_user(request):
    
    logout(request)
    return redirect('home')
    
def loginpage(request):
    form = forms.LoginForm()
    message =''
    if request.method =='POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username =form.cleaned_data['username'],
                password = form.cleaned_data ['password'],               
                   )
            if user is not None:
                login(request, user)
                return redirect('accueil')
            else:
                message = 'Identifiants invalides.'
    return render(request, 'authentication/login.html',
                  {'form': form, 'message': message})
def Sing_up(request):
    form = forms.SingForm()
    if request.method =='POST':
        form = forms.SingForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/sign.html',
                  context = {'form': form})

