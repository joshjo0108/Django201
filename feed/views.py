# from django.shortcuts import render <- function based VIEWS
# WE ARE GOING TO USE CLASS BASED VIEWS

from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from followers.models import Follower

from .models import Post

class HomePage(TemplateView):
    http_method_names = ['get']
    # SELF CONTAINED
    template_name = "feed/homepage.html"
    # FROM models.py's CLASS
# 1st method
    # model = Post            # USING THE MODEL FROM models.py
    # context_object_name = "posts"
    # queryset = Post.objects.all().order_by('-id')[0:30]
# 2nd method
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data( *args, **kwargs)
        if self.request.user.is_authenticated:
            following = list(
                Follower.objects.filter(followed_by=self.request.user).values_list('following', flat=True)
            )
            # IF YOU ARE NOT FOLLOWING ANYONE, JUST GIVE ME THE DEFAULT POSTS
            if not following:
                posts = Post.objects.all().order_by('-id')[0:30]
            # SHOW ONLY THE FOLLOWERS I'M FOLLOWING
            else:
                posts = Post.objects.filter(author__in=following).order_by('-id')[0:60]
        else:
            posts = Post.objects.all().order_by('-id')[0:30]
        # SIMILAR TO...<context['posts'] = Post.objects.all().order_by('-id')[0:30]>
    # "posts" IS USED IN "homepage.html"
        context['posts'] = posts
        return context


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