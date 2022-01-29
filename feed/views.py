# from django.shortcuts import render <- function based VIEWS
# WE ARE GOING TO USE CLASS BASED VIEWS

from django.views.generic import ListView
from .models import Post

class HomePage(ListView):
    http_method_names = ['get']
    # SELF CONTAINED
    template_name = "feed/homepage.html"
    # FROM models.py's CLASS
    model = Post            # USING THE MODEL FROM models.py
    context_object_name = "posts"
    queryset = Post.objects.all().order_by('-id')[0:30]
