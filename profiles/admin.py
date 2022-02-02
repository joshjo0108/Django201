from django.contrib import admin
from .models import Profile

# HERE BELOW WILL CREATE A AREA WE CAN POST STUFF
# REGISTERING
class ProfileAdmin(admin.ModelAdmin):
    pass

# CONNECTING 2 CLASSES: Post + PostAdmin
admin.site.register(Profile, ProfileAdmin)
