from django.shortcuts import render
from django.views import generic 
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy 

# in class defined views, must define form_class, template_name, and success_url

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')  # so that when you register you are directed to the login page 