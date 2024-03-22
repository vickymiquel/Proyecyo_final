from django.urls import path
from AppLogin.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", login, name = "login"),
    path("signup/", signup, name = "signup"),
    path("logout", LogoutView.as_view(template_name="AppLogin/logout.html"), name = "logout")
]