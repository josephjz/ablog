from django.contrib import admin
from .models import Post

# have to register any new models in our admin area 

admin.site.register(Post) # this allows our blog post entries to be accessible from blog post area, creates the Posts table on admin
