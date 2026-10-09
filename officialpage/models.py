from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
# Create your models here.

class Photo(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length =128, blank =True)# blank = True pour permettre aux l'utilisateur de laisser la champs vide  par defaut c'est False
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete =models.CASCADE)
    data_created = models.DateTimeField(auto_now_add =True)


class Blog(models.Model):
    photo = models.ForeignKey(Photo, null=True, 
    on_delete =models.SET_NULL, blank =True)
    title =models.CharField(max_length =128)
    content =models.CharField(max_length = 5000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete =models.CASCADE)
    date_created =models.DateTimeField(auto_now_add =True)
    starred = models.BooleanField(default=False)

# Liste des extensions autorisées (Images + PDF)
VALID_IMAGE_EXTENSIONS = ['pdf', 'jpg', 'jpeg', 'png']


class ActeMariage(models.Model):
    demandeur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='demandes_acte',
    )

    # Informations du Marié
    nom_marie = models.CharField(max_length=70, verbose_name='Nom du marié')
    prenom_marie = models.CharField(
        max_length=70, verbose_name='Prénom du marié'
    )
    # Remplacement par FileField + Validator
    cip_marie = models.FileField(
        upload_to='cip/maries/',
        verbose_name='CIP du marié (PDF ou Image)',
        validators=[
            FileExtensionValidator(allowed_extensions=VALID_IMAGE_EXTENSIONS)
        ],
    )
    image_epoux = models.ImageField()

    # Informations de l'Épouse
    nom_epouse = models.CharField(
        max_length=70, verbose_name='Nom de la mariée'
    )
    prenom_epouse = models.CharField(
        max_length=70, verbose_name='Prénom de la mariée'
    )
    image_epouse = models.ImageField(
        upload_to='photo/maries/',
        verbose_name ='Photo du marié',
        validators =[
            FileExtensionValidator(allowed_extensions = VALID_IMAGE_EXTENSIONS ) 
        ]

    )
    # Remplacement par FileField + Validator
    cip_epouse = models.FileField(
        upload_to='cip/epouses/',
        verbose_name='CIP de la mariée (PDF ou Image)',
        validators=[
            FileExtensionValidator (allowed_extensions=VALID_IMAGE_EXTENSIONS)
        ],
    )
    signature_du_mari = models.FileField(
    upload_to='signature/epoux/',
    verbose_name="Signature de l'époux (signez sur papier, scannez et envoyez)",
    validators=[
        FileExtensionValidator(
            allowed_extensions=VALID_IMAGE_EXTENSIONS
        )
    ],
    blank=True,
    null = True,
    )

    signature_de_la_mariee = models.FileField(
    upload_to='signature/epouse/',
    verbose_name="Signature de l'épouse (signez sur papier, scannez et envoyez)",
    validators=[
        FileExtensionValidator(
            allowed_extensions=VALID_IMAGE_EXTENSIONS
        )
    ],
    blank= True,
    null = True,
    )
    profession_epoux = models.CharField( max_length= 200, verbose_name= "Profession de l'époux", blank=True, null=True)
    profession_epouse = models.CharField( max_length=200,  verbose_name= "Profession de l'épouse", blank=True, null=True)

    # Informations du Mariage
    dot = models.CharField(max_length=100, verbose_name='Dot')
    date_mariage = models.DateField(verbose_name='Date du mariage')

    # Témoins
    temoin_1 = models.CharField(
        max_length=100, verbose_name='Nom et prénom du témoin 1'
    )
    temoin_2 = models.CharField(
        max_length=100, verbose_name='Nom et prénom du témoin 2'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Acte de mariage : {self.nom_marie} & {self.nom_epouse}'