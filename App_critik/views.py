from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import *
from django.contrib.auth import *
from App_critik.models import *
from App_critik.forms import *

def home(request):
    return render(request, "App_critik/home.html")

# PELICULAS
def add_movie(request):
    if request.method == "POST":

        form_1 = add_movie_form(request.POST)

        if form_1.is_valid():

            info = form_1.cleaned_data

            movie = new_movie(movie_name = info["movie_name"], movie_release_year = info["movie_release_year"], movie_genre = info["movie_genre"], movie_director = info["movie_director"],  movie_poster = info["movie_poster"])

            movie.save()

            return (request, "App_critik/movies/new_movie.html")
        
    else:
        form_1 = add_movie_form()

    return render(request, "App_critik/movies/add_movie.html", {"form_1":form_1})

def movies(request):
    return render(request, "App_critik/movies/all_movies.html")

# SERIES
def add_show(request):

    if request.method == "POST":

        form_2 = add_show_form(request.POST)

        if form_2.is_valid():

            info = form_2.cleaned_data

            show = new_show(show_name = info["show_name"], show_release_year = info["show_release_year"], show_director = info["show_director"], show_postere = info["show_poster"])
            
            show.save()

            return render(request, "App_critik/shows/new_show.html")
        
    else:
            form_2 = add_show_form()

    return render (request, "App_critik/shows/add_show.html", {"form_2":form_2})

def shows(request):
    return render(request, "App_critik/shows/all_shows.html")


def about(request):
    pass


# LOGIN / PERFIL 
def profile(requiest):
    pass

