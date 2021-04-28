from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from .forms import PostForm, EditForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
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

    # creating code that passes context dictonary stuff into our home page 
    # rememebr we did this with category view but that was function based
    # so now this is passing data with class based views 

    def get_context_data(self, *args, **kwargs):
        # query our category model of our data base to then create links out of all of them 
        cat_menu = Category.objects.all() # this grabs out everything in our cateogy model, namely the names and then assign it to the var
        # since our cateorgy model only has the name field, we dont need to filter and pull out the names, we ca just pull out everyitng (which is the name)
        # lastly need to push  cat_menu onto the page as a context dictionary that we can then access 
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        # super(_,) where _ is the view we are in 
        context["cat_menu"] = cat_menu
        return context  # so now we can access "cat_menu" from our home page

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        # query our category model of our data base to then create links out of all of them 
        cat_menu = Category.objects.all() # this grabs out everything in our cateogy model, namely the names and then assign it to the var
        # since our cateorgy model only has the name field, we dont need to filter and pull out the names, we ca just pull out everyitng (which is the name)
        # lastly need to push  cat_menu onto the page as a context dictionary that we can then access 
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs) # dont forget to change the super(_) for which view we are now working with 
        # super(_,) where _ is the view we are in 
        context["cat_menu"] = cat_menu
        
        # look up what post we are looking at, look it up in db Post, find post with id of primary key 
        stuff = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()   # rememebr we created this total likes() function in model
        # adding another context variable to pass in likes 
        context["total_likes"] = total_likes

        liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True 
        context["liked"] = liked
        
        return context  # so now we can access "cat_menu" from our home page

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

def CategoryView(request, cats): # remember this (cats) is what we named it on the urls.py file; it is a string variable, the cats that gets passed is now going to have a - from our html...

    # now we need to query the database 
    # before in the class based views they were doing this for us 
    # just the posts of the specific cats category

    category_posts = Post.objects.filter(category=cats.replace('-',' '))    # so we use a little bit of python to replace all - with a space
    # Post.objects queries our post model   
    # category is a field in our post model
    # now category_post is an object, so we can pass it into our html 

    # dont know how to do the equivalent of get_context_data for the function based view, but trying here
    cat_menu_list = Category.objects.all()
                                                                # so that the title in the html tag comes up with spacee instead of - 
    return render(request, 'categories.html', {'cats': cats.title().replace('-',' '), 'category_posts':category_posts, 'cat_menu_list':cat_menu_list}) #.title makes it cap
        # third param of function based views return render() is the context directory, these objects are then recognized by that html page 
        # can use bots cats and category_posts as vars on categories.html now 

def CategoryListView(request): 
    # categories page which is linked in the nav bar 
    # query the data base like we did in HomeView
    cat_menu_list = Category.objects.all() # this grabs out everything in our category model, namely the names and then assign it to the var
    # pass this query into our page 

    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list}) 

def LikeView(request, pk):
    # when this gets called, we have liked a post 
    # need to save that to the db, knowing which post and saving it as a like 
    # use get object here -- this requires an import 

    post = get_object_or_404(Post, id = request.POST.get('post_id')) # look up our post table, and grab id that equals request.post.get('post_id')
    # this is post id because of the name param in button on article detials page 

    liked = False 
    if post.likes.filter(id = request.user.id).exists():
        # make it a dislike button 
        post.likes.remove(request.user)
        liked = True
    else:
        post.likes.add(request.user)
        liked = True # adds a like for whoever clicked the like button 

    # when clicking the home button we dont want the page to switch
    return HttpResponseRedirect(reverse('article-detail', args = [str(pk)]))









