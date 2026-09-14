
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.conf.urls.static import static
import officialpage.views 
import authentication.views
urlpatterns = [
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
    path('accueil/', officialpage.views.demande, name ='accueil'),
    path('signup/', authentication.views.Sing_up, name ='signup'),
    path('upload/', officialpage.views.photo_upload, name='upload'),
    path('photo/upload', officialpage.views.photo_upload, name ='photo_upload')
    ]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
    
