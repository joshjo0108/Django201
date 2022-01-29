from django.contrib import admin
from .models import Post

# HERE BELOW WILL CREATE A AREA WE CAN POST STUFF
# REGISTERING
class PostAdmin(admin.ModelAdmin):
    pass

# CONNECTING 2 CLASSES: Post + PostAdmin
admin.site.register(Post, PostAdmin)
