"""ablog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# copied and pasted the code written in project wide urls.py, created a new app urls.py file, and pasted the code here 

# deleted admin import 
from django.urls import path  # deleted include import
# from . import views # this is what we have for function based views 
from .views import HomeView, ArticleDetailView

urlpatterns = [
    # deleted paths from project wide urls.py, instead writing new ones 
    #path('', views.home, name = "home")  # this name is the function name in the views.py file, which we need to go create in urls.py

    # now we need class based views urls 
    path('', HomeView.as_view(), name = "home"), # home page 
    path('article/<int:pk>', ArticleDetailView.as_view(), name = "article-detail")   # BIG NOTE: each blog post has its own primary key, makes every post unique
]
