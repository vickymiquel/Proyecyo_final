from django.urls import path
from AppLogin.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # LOGIN
    path("login/", login_view, name = "login"),
    path("login_complete/", login_complete),

    # SIGNUP
    path("signup/", signup, name = "signup"),
    path("signup_complete", signup_complete),

    # LOGOUT
    path("logout/", LogoutView.as_view(template_name="logout.html"), name = "logout"),

    # EDIT USER
    path("edit_user/", edit_user, name = "edit_user"),
    path("edit_complete/", edit_complete),

    # AVATAR
    path("avatar/", upload_avatar, name = "avatar"),
    path("avatar_complete", avatar_complete)
]