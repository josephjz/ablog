from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs = {'class': 'form-control'} ))
    first_name = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'class': 'form-control'} ))
    last_name = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'class': 'form-control'} )) 
    username = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'class': 'form-control'} ))  
    last_login = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'class': 'form-control'} ))
    is_superuser = forms.CharField(max_length = 100, widget = forms.CheckboxInput(attrs = {'class': 'form-check'} ))
    is_staff = forms.CharField(max_length = 100, widget = forms.CheckboxInput(attrs = {'class': 'form-check'} ))
    is_active = forms.CharField(max_length = 100, widget = forms.CheckboxInput(attrs = {'class': 'form-check'} ))
    date_joined = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'class': 'form-control'} ))

    class Meta:
        model = User # quick note on fields below -- the order of fields is order they will show up on page 
        fields = ('username','first_name','last_name','email','password','last_login','is_superuser','is_staff', 'is_active','date_joined')
        # if there are fields you don't want, just do't include them in this class Meta fields section 
        