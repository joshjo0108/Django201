from django.contrib import admin
from .models import Follower

# HERE BELOW WILL CREATE A AREA WE CAN POST STUFF
# REGISTERING
class FollowerAdmin(admin.ModelAdmin):
    pass

# CONNECTING 2 CLASSES: Follower + FollowerAdmin
admin.site.register(Follower, FollowerAdmin)
