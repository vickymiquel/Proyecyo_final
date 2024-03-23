from django.urls import path
from AppLogin.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", login_view, name = "login"),
    path("login_complete/", login_complete),
    path("signup/", signup, name = "signup"),
    path("signup_complete", signup_complete),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name = "logout"),
    path("edit_user/", edit_user, name = "edit_user"),
    path("edit_complete/", edit_complete)
]