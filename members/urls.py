# whenever you make a new app, you have to create this urls file 
# also whenever you create a new app, add it to SETTINGS.PY FILE INSTALLED APPS 

from django.urls import path  # deleted include import
from . import views # this is what we have for function based views 

from .views import UserRegisterView, UserLoginView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView

from django.contrib.auth import views as auth_views # allows us to use some views with the built in authenticaiton systme

# PasswordChangeView built in, PasswordsChangeView is what we made 

urlpatterns = [
    path('login/',UserLoginView.as_view(), name = 'login'),
    path('register/',UserRegisterView.as_view(), name = 'register'), 
    path('edit_profile/',UserEditView.as_view(), name = 'edit_profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name = 'registration/change-password.html'), name = 'password'), # if you do this without template name, it looks like django admin side for changing a password
    path('password/', PasswordsChangeView.as_view(template_name = 'registration/change-password.html'), name = 'password'),
    path('password_success', views.password_success, name = "password_success"),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name = 'show_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name = 'edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name = 'create_profile_page'),
]
