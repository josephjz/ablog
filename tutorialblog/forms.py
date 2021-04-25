# in order to style our django forms used to make blog posts, we need to create a form  

from django import forms
from .models import Post 

# create a class 
# inherits forms.ModelForm which allows us to create form fields for our model (post model)
class PostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = {
            # fields are the fields from the model 
            'title',
            'title_tag', 
            'author', 
            'body'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter a post title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter a post title tag'}),
            'author': forms.Select(attrs={'class':'form-control'}), # this is a drop down, aka select drop down
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'What is on your mind today?'}), # this is a body, which is a text area 
        }

class EditForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = { # not editing the author 
            'title',
            'title_tag',
            'body'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter a post title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter a post title tag'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'What is on your mind today?'}), # this is a body, which is a text area 
        }

