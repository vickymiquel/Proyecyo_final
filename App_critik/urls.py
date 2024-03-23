from django.urls import path
from App_critik.views import *

urlpatterns = [
    path('', home, name = "home"),

    # PELICULAS
    path('movies/', movies, name = "movies"),
    path('add_movie/', add_movie, name = "add_movie"),
    path('movie_info/<int:id>', view_movie, name = "movie_info"),

    # SERIES
    path('shows/', shows, name = "shows"),
    path('add_show/', add_show, name = "add_show"),

    # SOBRE NOSOTROS
    path('about/', about, name = "about"),
    
    # PERFIL
    path('profile/', profile, name = "profile"), 
] 