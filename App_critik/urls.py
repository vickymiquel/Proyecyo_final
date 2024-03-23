from django.urls import path
from App_critik.views import *

urlpatterns = [
    path('', home, name = "home"),

    # PELICULAS
    path('movies/', movies, name = "movies"),
    path('add_movie/', add_movie, name = "add_movie"),
    path('movie_info/<int:movie_id>', view_movie, name = "movie_info"),
    path('search_movie/', search_movie, name="search_movie"),
    path('search_movie_results/', search_movie_results, name="search_show_movie"),



    # SERIES
    path('shows/', shows, name = "shows"),
    path('add_show/', add_show, name = "add_show"),
    path('new_review/<int:show_id>', show_review, name = "new_review"),
    path('show_info/<int:show_id>', view_show, name = "show_info"),
    path('show_review/', show_review, name = "show_review"),
    path('search_show/', search_show, name="search_show"),
    path('search_show_results/', search_show_results, name="search_show_results"),


    # SOBRE NOSOTROS
    path('about/', about, name = "about"),
    
    # PERFIL
    path('profile/', profile, name = "profile"), 
] 