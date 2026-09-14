from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
# Create your views here.

def home(request):
    return render (request, 'officialpage/home.html')
@login_required
def demande(request):
    photos = models.Photo.objects.all()
    return render(request, 'officialpage/accueil.html', context={'photos': photos})
@login_required
def photo_upload(request):
    form = forms.PhotoForm()
    if request.method =='POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        photo = form.save(commit =False)
        photo.uploader = request.user
        photo.save()
        return redirect('accueil')
    return render(request,'officialpage/photo_upload.html', context={'form':form})
