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


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required = True, widget = forms.EmailInput(attrs = {'class': 'form-control'} ))
    first_name = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'class': 'form-control'} ))
    last_name = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'class': 'form-control'} ))

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')
    
    # NOTE: we needed to add this init function to handle the styling of the fields that are built into the django user 
    # userename passwords 
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'