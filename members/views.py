from django.shortcuts import render, get_object_or_404
from django.views import generic 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy 
from .forms import SignUpForm, LoginForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from .models import Member
from django.views.generic import DetailView, CreateView
# in class defined views, must define form_class, template_name, and success_url

from tutorialblog.models import Profile

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

def password_success(request):
    return render(request, 'registration/password_success.html', {})

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm # ours
    #success_url = reverse_lazy('home')
    success_url = reverse_lazy('password_success') # this reverse lazy is to the name given in urls

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        #users = Profile.objects.all() 
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id = self.kwargs['pk']) # grab only specific user  
        context["page_user"] = page_user
     
        return context  # so now we can access "cat_menu" from our home page

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'website_url', 'insta_url', 'twitter_url', 'fb_url']
    success_url = reverse_lazy('home')

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'


    # allows for knowing which user is filling out this form 
    # form will pass the user

    def form_valid(self, form):
        form.instance.user = self.request.user # there is a user filling out this form, lets grab them and make it availabel to the form
        return super().form_valid(form) # passing in the form that has been submitted on this page 

    # so user id available to profile, so that this form gets saved to the right user id 

