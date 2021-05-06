from django.shortcuts import render
from django.views import generic 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy 
from .forms import SignUpForm, LoginForm, EditProfileForm
from .models import Member

# in class defined views, must define form_class, template_name, and success_url

# this is the built in one 
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')  # so that when you register you are directed to the login page 

# adding a login view 
class UserLoginView(generic.CreateView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user # will pass in the current user 