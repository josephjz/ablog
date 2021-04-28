from django.contrib import admin
from .models import Post, Category
# have to register any new models in our admin area 

admin.site.register(Post) # this allows our blog post entries to be accessible from blog post area, creates the Posts table on admin
admin.site.register(Category)
