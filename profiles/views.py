from django.contrib.auth.models import User
from django.views.generic import DetailView

from feed.models import Post

class ProfileDetailView(DetailView):
    http_methods_names = ["get"]
    template_name = "profiles/detail.html"
    model = User
    context_object_name = "user" 
    # LOOK UP THE USER BY "username"
    slug_field = "username"
    # COMING FROM "<str:username>/" <- IN "profiles/urls.py"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        # GETS THE OBJECT "user"
        user = self.get_object()
        context = super().get_context_data(**kwargs)
        context['total_posts'] = Post.objects.filter(author = user).count()
        # context['total_followers'] = ...
        return context