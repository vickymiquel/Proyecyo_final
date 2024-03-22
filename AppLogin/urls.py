from django.urls import path
from AppLogin.views import *

urlpatterns = [
    path("login/", login, name = "login"),
    path("signup/", signup, name = "signup")
]