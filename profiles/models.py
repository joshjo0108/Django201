from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField

class Profile(models.Model):
    user = models.OneToOneField(
        User,  #Django user
        on_delete=models.CASCADE,
        related_name="profile"
    )
    image = ImageField(upload_to='profiles')

    def __str__(self):
        return self.user.username

# CHECK TO SEE WHAT KIND OF DATA IS COMING IN 
# IF A USER CREATED AND SAVED, CREATE A USER IN "Profiles"
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a new Profile() object when a Django User is Created"""
    if created:
        Profile.objects.create(user=instance)