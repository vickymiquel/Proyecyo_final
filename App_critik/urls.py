from django.urls import path
from App_critik.views import *

urlpatterns = [
    path('', home, name = "home"),

    # PELICULAS
    path('movies/', movies, name = "movies"),
    path('add_movie/', add_movie, name = "add_movie"),
    path('movie_info/<int:movie_id>', view_movie, name = "movie_info"),
    path("edit_movie/<Movie_name>/", update_movie, name = "edit_movie"),
    path("delete_movies/<Movie_name>/", delete_movie, name = "delete_movie"),
    path("delete_complete_movie/", delete_complete_movie),

    # SERIES
    path('shows/', shows, name = "shows"),
    path('add_show/', add_show, name = "add_show"),
    path('new_review/', show_review, name = "new_review"),
    path('show_info/<int:show_id>', view_show, name = "show_info"),
    path("edit_show/<Show_name>/", update_show, name = "edit_show"),
    path("delete_show/<Show_name>/", delete_show, name = "delete_show"),
    path("delete_complete_show/", delete_complete_show),

    # SOBRE NOSOTROS
    path('about/', about, name = "about"),
    
] 