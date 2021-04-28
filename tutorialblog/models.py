from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse
from datetime import datetime, date


# this is a lil more involved than we need for the majors, but could work
class Category(models.Model):
    name =  models.CharField(max_length = 255)
    def __str__(self):
        return self.name #lets us see category name on the admin back end 

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length = 255)
    title_tag = models.CharField(max_length = 255)#, default = "My Freaking Awesome Blog")
    author = models.ForeignKey(User, on_delete = models.CASCADE) # deletes blog post from a user that has been deleted
                                                                # think about adding this for Biblio
    # the author field is ForeignKey key on the User model, which is a part of the django admin system 
    category = models.CharField(max_length = 255, default = 'uncategorized')
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True) # will happen automatically when new blog posts are created 

    def __str__(self):
        return self.title + ' | ' + str(self.author)   #lets us see title and author on the admin back end 

    def get_absolute_url(self):
        return reverse('home')
        # this will return to the home page, with this new upload 
        
        #return reverse('article-detail', args = (str(self.id)))
        # this will take it to the post that was just created!
        # want to point this back to the articles page 
        # any time seomthing is created in our model, it gets an id (kinda the same thing as primary key )
