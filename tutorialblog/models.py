from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length = 255)
    title_tag = models.CharField(max_length = 255, default = "My Freaking Awesome Blog")
    author = models.ForeignKey(User, on_delete = models.CASCADE) # deletes blog post from a user that has been deleted
                                                                # think about adding this for Biblio
    # ForeignKey key is from the User 
    
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)   #lets us see title and author on the admin back end 

