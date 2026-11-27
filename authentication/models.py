from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.forms.fields import CharField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=150)       # plus unique : plusieurs personnes peuvent avoir le même nom
    email = models.EmailField(unique=True)             # l'e-mail, lui, est unique
    profile_photo = models.ImageField(verbose_name='photo de profil')

    USERNAME_FIELD = 'email'                           
    REQUIRED_FIELDS = ['username']