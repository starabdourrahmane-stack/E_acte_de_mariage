from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from . import forms
from . import models
# Create your views here.

def home(request):
    return render (request, 'officialpage/home.html')
@login_required
def demande(request):
    photos = models.Photo.objects.all()
    return render(request, 'officialpage/accueilx.html', context={'photos': photos})
@login_required
def photo_upload(request):
    form = forms.PhotoForm()
    if request.method =='POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        photo = form.save(commit =False)
        photo.uploader = request.user
        photo.save()
        return redirect('accueilx')
    return render(request,'officialpage/photo_upload.html', context={'form':form})
@login_required
def officialpage_and_photo_upload(request):
    officialpage_form = forms.officialpageForm()
    photo_form = forms.PhotoForm()
    context = {
        'officialpage_form': officialpage_form,
        'photo_form': photo_form,
    }

    if request.method == 'POST':
        officialpage_form = forms.officialpageForm(request.POST)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        if all ([officialpage_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit =False)
            photo.uploader = request.user
            photo.save()
            officialpage = officialpage_form.save(commit =False)
            officialpage.author = request.user
            officialpage.photo = photo
            officialpage.save()
            return redirect ('home')
        # handle the POST request here
        context = {
            'officialpage_form': officialpage_form,
            'photo_form': photo_form,
    }
    return render(request, 'officialpage/create_blog_post.html', context = context)
@login_required
def formulaire_Mariage(request):
    form = forms.FromMariage()
    if request.method =='POST':
        form = forms.FromMariage(request.POST, request.FILES)
        if form.is_valid():
            acte = form.save(commit=False)
            acte.demandeur = request.user
            acte.save()
            return redirect('payer')
    return render(request, 'officialpage/formulaire.html',
                context={'form':form } )
@login_required
def payer(request):
    return render(request, 'officialpage/payer.html')
@login_required
def edit_officialpage(request, official_id):
    official = get_object_or_404(models.Blog, id = official_id)
    edit_form = forms.officialpageForm(instance=official)
    delete_form = forms.DeleteBlogForm()
    if request.methode =='POST':
        edit_form = forms.officialpageForm(request.POST, instance=official)
        if 'edit_officialpage' in request.POST:
            edit_form = forms.officialpageForm(request.POST, instance = official )
            edit_form.save()
            return redirect('home')
        if 'delete_officialpage' in request.POST:
            delete_form = forms.DeleteofficialpageForm(request.POST)
            if delete_form.is_valid():
                official.delete()
                return('accueilx')
    context = {
        'edit_form' :edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'officialpage/edit_officialpage.html', context =context)