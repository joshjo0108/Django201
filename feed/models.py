from django.db import models

class Post(models.Model):
    # THIS VARIABLES ARE MANAGED IN "migrations" FILES
    # VARIABLES: "1. id", "2. text"
    text = models.CharField(max_length=240)
