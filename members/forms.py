from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Member


# create a class 
# inherits forms.ModelForm which allows us to create form fields for our model (post model)

class LoginForm(forms.ModelForm):
    class Meta: 
        #model = Member
        model = User
        fields = {
            # fields are the fields from the model 
            'username',
            'password',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'password': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Password'}),
        }


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True, widget = forms.EmailInput(attrs = {'class': 'form-control'} ))
    username = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(max_length=30, required=True)
    password2 = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model = User
        fields = ('email','username', 'password1', 'password2')