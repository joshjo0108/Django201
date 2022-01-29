from django.db import models

class Post(models.Model):
    # THIS VARIABLES ARE MANAGED IN "migrations" FILES
    # VARIABLES: "1. id", "2. text"
    text = models.CharField(max_length=240)
    # AFTER THIS VARIABLE
    # RUN: python3 manage.py makemigrations & python3 manage.py migrate
    date = models.DateTimeField(auto_now=True)


    # SHOW WHAT YOU WROTE ON POST 
    def __str__(self):
        return self.text[0:100]
