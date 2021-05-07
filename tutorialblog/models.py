from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse
from datetime import datetime, date

from ckeditor.fields import RichTextField # for rich text editor 


# this is a lil more involved than we need for the majors, but could work
class Category(models.Model):
    name =  models.CharField(max_length = 255)
    def __str__(self):
        return self.name #lets us see category name on the admin back end 

    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    # need to associate this model with our User model with one to one 
    user = models.OneToOneField(User, null= True, on_delete = models.CASCADE)
    bio = models.TextField()

    profile_pic = models.ImageField(null = True, blank = True, upload_to = "images/profile/")
    insta_url = models.CharField(max_length = 255, null = True, blank = True)
    twitter_url = models.CharField(max_length = 255, null = True, blank = True)
    website_url = models.CharField(max_length = 255, null = True, blank = True)
    fb_url = models.CharField(max_length = 255, null = True, blank = True)
    
    def __str__(self):
        return str(self.user)

class Post(models.Model):
    title = models.CharField(max_length = 255)
    header_image = models.ImageField(null = True, blank = True, upload_to = "images/")
    title_tag = models.CharField(max_length = 255)#, default = "My Freaking Awesome Blog")
    author = models.ForeignKey(User, on_delete = models.CASCADE) # deletes blog post from a user that has been deleted
                                                                # think about adding this for Biblio
    # the author field is ForeignKey key on the User model, which is a part of the django admin system 
    category = models.CharField(max_length = 255, default = 'uncategorized')
    #body = models.TextField()
    body = RichTextField(blank = True, null = True) # always migrate when you change models
    post_date = models.DateField(auto_now_add=True) # will happen automatically when new blog posts are created 
    snippet = models.CharField(max_length = 255)

    # adding a new field for likes 
    # using many to many becuase we are associating iff things from diff tables 
    # any time we change the data baes must make a migration
    likes = models.ManyToManyField(User, related_name = 'blog_post') 

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)   #lets us see title and author on the admin back end 

    def get_absolute_url(self):
        return reverse('home')
        # this will return to the home page, with this new upload 
        
        #return reverse('article-detail', args = (str(self.id)))
        # this will take it to the post that was just created!
        # want to point this back to the articles page 
        # any time seomthing is created in our model, it gets an id (kinda the same thing as primary key )
