# in order to style our django forms used to make blog posts, we need to create a form  

from django import forms
from .models import Post, Category 

# hard coded
#choices = [('Coding','Coding'), ('Sports','Sports'), ('Music','Music'),]

# vs
# dynamically query database category model in backend 
# this is 'name' because of the field in our model! 
choices = Category.objects.all().values_list('name','name')
# to put these into the drop down, we need to loop through these and create a list 
choice_list = [] #empty list 

for item in choices:
    choice_list.append(item)

# so now we have a easy list instead of a weird query object

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
            'category',
            'body',
            'snippet',
        }

        # note: before for loggedin/authenticating user, we used user.id but that is only known to the front end 
        # the backend does not know it so we need to work around this author drop down 
        # to only give us the appropriate author 
        # we are going to hack around with javascript 


        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your post title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter a post title tag'}),
            #'author_deleted': forms.Select(attrs={'class':'form-control'}), # this is a drop down, aka select drop down
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'type':'hidden','id':'elder'}), # we add and id for this textbox to write some javascript with it in add post page, it is a css id
            'category': forms.Select(choices = choice_list, attrs={'class':'form-control'}), # these are hard coded choices; would get error if you put attrs first 
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'What is on your mind today?'}), # this is a body, which is a text area 
            'snippet': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Preview text'}), # this is a body, which is a text area 
        }

class EditForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = { # not editing the author 
            'title',
            'title_tag',
            'body', 
            'snippet'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter a post title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter a post title tag'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'What is on your mind today?'}), # this is a body, which is a text area 
            'snippet': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Preview '}), # this is a body, which is a text area 
        }

