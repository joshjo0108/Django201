# from django.shortcuts import render <- function based VIEWS
# WE ARE GOING TO USE CLASS BASED VIEWS

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .models import Post

class HomePage(ListView):
    http_method_names = ['get']
    # SELF CONTAINED
    template_name = "feed/homepage.html"
    # FROM models.py's CLASS
    model = Post            # USING THE MODEL FROM models.py
    context_object_name = "posts"
    queryset = Post.objects.all().order_by('-id')[0:30]


class PostDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "feed/detail.html"
    model = Post
    Postcontext_object_name = "post"

# IF THE USER IS NOT LOGGED IN, KICK HIM OUT! -> "LoginRequiredMixin"
# IF YOU ARE LOGGED IN, PERFORM YOUR REGULAR TASKS -> "CreateView"
class CreateNewPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "feed/create.html"
    fields = ['text']
    # HOME PAGE
    success_url = "/"

# "dispatch" IS RAN BEFORE "form_valid"
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # NOT SAVE IT
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        # "Post" IS FROM "models.py" <- IT CONTAINS text, date, author
        post = Post.objects.create(
            # "text" IS THE KEY, AND IT WILL RETURN THE VALUE
            # THIS IS COMING FROM, "main.js"->"$.ajax"
            text = request.POST.get("text"),
            author = request.user,
        )
        return render(
            request,
            "includes/post.html",
            {
                "post":post,
                "show_detail_link": True,
            },
            content_type="application/html"
        )