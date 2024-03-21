from django.urls import path
from App_critik.views import *

urlpatterns = [
    path('', home, name = "home"),
    path('movies', movies, name = "movies"),
    path('shows', shows, name = "shows"),
    path('about', about, name = "about"),
    path('profile', profile, name = "profile"),
]