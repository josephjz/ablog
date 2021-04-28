from django.shortcuts import render
from .models import Post, Category
from .forms import PostForm, EditForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
                                                      # these are generic views that make query sets to data base for us 
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
    # ordering = ['-id'] # helpful to look at the migrations to see this id in action
    ordering = ['-post_date']

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

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category # this tells the view to use the post model 
    #form_class = PostForm # but we also need to tell it to use our post form 
    template_name = 'add_category.html'
    # designate the fields for this page 
    fields = '__all__' # remember we need either form_class or to name fields 


# AYE going to do a function based view for fun 

def CategoryView(request, cats): # remember this (cats) is what we named it on the urls.py file; it is a string variable 

    # now we need to query the database 
    # before in the class based views they were doing this for us 
    # just the posts of the specific cats category

    category_posts = Post.objects.filter(category=cats)
    # Post.objects queries our post model 
    # category is a field in our post model
    # now category_post is an object, so we can pass it into our html 

    return render(request, 'categories.html', {'cats': cats.title(), 'category_posts':category_posts}) #.title makes it cap
        # third param of function based views return render() is the context directory, these objects are then recognized by that html page 
        # can use bots cats and category_posts as vars on categories.html now 







