from django.shortcuts import render
from .models import Post
from .forms import PostForm, EditForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView # these are generic views that make query sets to data base for us 
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

class AddPostView(CreateView):
    model = Post # this tells the view to use the post model 
    form_class = PostForm # but we also need to tell it to use our post form 
    template_name = 'add_post.html'
    # designate the fields for this page 
    # fields = ('title', 'body')    THIS DID NOT WORK
    # fields = '__all__' since we are now using the post form, we dont want to use this fields thing anymore (might be problematic)

class UpdatePostView(UpdateView): # by passing in UpdatView we dont need to do the form_class thing that will happen automatically 
    model = Post
    form_class = EditForm # note you cant have both a form class and a fields 
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag','body']






