from django.urls import path
from . import views

# MATCHES THE APP NAME WE ARE USING FROM app.py
app_name = "feed"

urlpatterns = [
    path("", views.HomePage.as_view(), name="index")
]