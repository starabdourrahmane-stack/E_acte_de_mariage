
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from django.conf.urls.static import static
import officialpage.views 
import authentication.views
urlpatterns = [
    path('',officialpage.views.home),
    path('admin/', admin.site.urls),
    path('home/', officialpage.views.home, name='home'),
    path('login/', authentication.views.loginpage, name ='login'),
    path('logout_user', authentication.views.logout_user, name = 'logout'),

    path('change-password/', PasswordChangeView.as_view( template_name='authentication/password_change_form.html'),
         name ='password_change'),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'),
         name='password_change_done'
         ),
    path('', include('django.contrib.auth.urls')),
    path('accueilx/', officialpage.views.demande, name ='accueilx'),
    path('signup/', authentication.views.Sing_up, name ='signup'),
    path('upload/', officialpage.views.photo_upload, name='upload'),
    path('profile-photo/upload', authentication.views.upload_profile_photo, name='changephoto'),
    path('photo/upload', officialpage.views.photo_upload, name ='photo_upload'),
    path('officialpage/create', officialpage.views.officialpage_and_photo_upload, name ='create_blog_post'),
    path('officialpage/remplissage', officialpage.views.formulaire_Mariage, name ='formulaire'),
    path('payement/', officialpage.views.payer, name= 'payement'),
    path('mariage_islam/', officialpage.views.mariage_islam, name='mariage_islam'),
    path('confidentialite/', officialpage.views.confidentialite, name='confidentialite'),
    path('contact/', officialpage.views.contact_us, name='contact_us'),
    path('signer/', officialpage.views.signer, name='signature'),
    path('identification/', officialpage.views.identification, name= 'exemple'),
    
    path(
        'password-reset/',
        PasswordResetView.as_view(
            template_name='authentication/password_reset.html',
            email_template_name='authentication/password_reset_email.txt',
            subject_template_name='authentication/password_reset_subject.txt',
            success_url='/password-reset/done/'
        ),
        name='password_reset'
    ),

    path(
        'password-reset/done/',
        PasswordResetDoneView.as_view(
            template_name='authentication/password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='authentication/password_reset_confirm.html',
            success_url='/reset/done/'
        ),
        name='password_reset_confirm'
    ),

    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(
            template_name='authentication/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]
    # Restauration du mot de passe en cas d'oublie
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
    
