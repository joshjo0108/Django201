from django.contrib.auth.models import User
from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest, JsonResponse
from feed.models import Post
from followers.models import Follower

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

class FollowView(LoginRequiredMixin, View):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        # WORKING WITH DICTIONARY
        data = request.POST.dict()

        if "action" not in data or "username" not in data:
            return HttpResponseBadRequest("Missing data")

        try:
            other_user = User.objects.get(username=data['username'])
        except User.DoesNotExist:
            return HttpResponseBadRequest("Missing user")

        # WHEN FOLLOWING
        if data['action'] == "follow":
            follower, created = Follower.objects.get_or_create(
                followed_by = request.user,
                following = other_user
            )
        # WHEN UNFOLLOWING
        else:
            try:
                follower = Follower.objects.get(
                    followed_by = request.user,
                    following = other_user,
                )
            except Follower.DoesNotExist:
                follower = None
            if follower:
                follower.delete()

        return JsonResponse({
            'success':True,
            'wording': "Unfollow" if data['action']=="follow" else "Follow"
        })