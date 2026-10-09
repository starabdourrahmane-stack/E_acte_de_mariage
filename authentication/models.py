from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    CREATOR ='CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'


    ROLE_CHOICES =(
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné'),
)
    
    profile_photo = models.ImageField(verbose_name='photo de profil')
    role = models.CharField(max_length= 30, choices= ROLE_CHOICES,)
