from django import forms
from . import models

class PhotoForm(forms.ModelForm):
    class Meta:
        model =models.Photo
        fields =['image', 'caption']

class officialpageForm(forms.ModelForm):
    edit_officialpage =forms.BooleanField(widget =forms.HiddenInput,
                initial=True)
    class Meta:
        model = models.Blog
        fields = ['title', 'content']


class DeleteofficialpageForm(forms.Form):
    delete_officialpage = forms.BooleanField(widget = forms.HiddenInput, 
                initial=True)
class FromMariage(forms.ModelForm):
    class Meta:
        model = models.ActeMariage
        fields = ['nom_marie', 'prenom_marie', 'cip_marie', 'image_epoux', 'nom_epouse', 'prenom_epouse', 
                  'image_epouse','cip_epouse','dot','date_mariage','temoin_1','temoin_2','profession_epoux',
            'profession_epouse',
            'signature_du_mari',
            'signature_de_la_mariee',

                  ]
        widgets = {
            'cip_epouse':forms.FileInput(attrs={'accept':'application/pdf,image/*'}),
            'cip_marie': forms.FileInput(
                attrs={'accept': 'application/pdf,image/*'}
            ),
            'image_epoux': forms.FileInput(attrs={'accept':'application/pdf, image/*'}),
            'image_epouse': forms.FileInput(attrs={'accept':'application/pdf, image/*'}),
             'date_mariage': forms.DateTimeInput(attrs= {'type': 'date'},
                format='%Y-%m-%d'
            ),
        }
