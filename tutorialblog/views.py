from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView # these are generic views that make query sets to data base for us 
                                                      # list for all of our blog posts 
                                                      # detail to view one blog post 
                                                      # makes the process much easier, but might not be compatible with biblio

# Create your views here.

# this is old #def home(request): 
    #return render(request,'home.html',{})

# class based views ------ NOTE: THESE AREN'T FUNCTION BASED LIKE WE HAVE BEEN DOING 

class HomeView(ListView): # normally we pass in the request
    # want to list all of the blog posts on the homepage using the post model 
    model = Post    # note the difference here too of using Post not User 
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'






