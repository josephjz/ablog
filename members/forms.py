from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import Member
from tutorialblog.models import Profile 

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


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'form-control', 'type':'password'}))
    new_password1 = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'form-control', 'type':'password'}))
    new_password2 = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'form-control', 'type':'password'}))

    class Meta:
        model = User
        fields = ('old_password','new_password1', 'new_password2')

class ProfilePageForm(forms.ModelForm):
    class Meta: 
        model = Profile
        # note that we have left off user, becuaes we do not want them to be able to choose who the user is 
        fields = ('bio', 'profile_pic', 'insta_url', 'twitter_url', 'website_url', 'fb_url')

        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Bio Section'}),
            #'profile_pic': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter a post title tag'}),
            'insta_url': forms.TextInput(attrs={'class':'form-control'}), # we add and id for this textbox to write some javascript with it in add post page, it is a css id
            'twitter_url': forms.TextInput(attrs={'class':'form-control'}), # these are hard coded choices; would get error if you put attrs first 
            'website_url': forms.TextInput(attrs={'class':'form-control'}), # this is a body, which is a text area 
            'fb_url': forms.TextInput(attrs={'class':'form-control'}), # this is a body, which is a text area 
        }

