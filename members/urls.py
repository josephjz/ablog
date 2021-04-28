# whenever you make a new app, you have to create this urls file 
# also whenever you create a new app, add it to SETTINGS.PY FILE INSTALLED APPS 

from django.urls import path  # deleted include import
# from . import views # this is what we have for function based views 

from .views import UserRegisterView, UserLoginView #, RegistrationView

urlpatterns = [
    path('login/',UserLoginView.as_view(), name = 'login'),
    path('register/',UserRegisterView.as_view(), name = 'register'), 
    #path('register/',RegistrationView.as_view(), name = 'register'),
]
