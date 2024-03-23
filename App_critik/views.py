from django.shortcuts import render, get_object_or_404
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

        form_1 = add_movie_form(request.POST, request.FILES)

        if form_1.is_valid():

            info = form_1.cleaned_data

            movie = new_movie(
                movie_name = info["movie_name"], 
                movie_release_year = info["movie_release_year"], 
                movie_genre = info["movie_genre"], 
                movie_director = info["movie_director"], 
                movie_protagonist = info["movie_protagonist"], 
                movie_poster = info["movie_poster"]
            )

            movie.save()

            return (request, "App_critik/movies/new_movie.html")
        
    else:
        form_1 = add_movie_form()

    return render(request, "App_critik/movies/add_movie.html", {"form_1":form_1})

def movies(request):
    movie_catalogue = new_movie.objects.all()
    return render(request, "App_critik/movies/all_movies.html", {"movie_catalogue": movie_catalogue})

def view_movie(request, movie_id):
    selected_movie = get_object_or_404(new_movie, pk = movie_id)

    return render(request, "App_critik/movies/movie.html", {"selected_movie":selected_movie})






# SERIES
def add_show(request):

    if request.method == "POST":

        form_2 = add_show_form(request.POST, request.FILES)

        if form_2.is_valid():

            info = form_2.cleaned_data

            show = new_show(
                show_name = info["show_name"],
                show_release_year = info["show_release_year"], 
                show_genre = info["show_genre"], 
                show_director = info["show_director"], 
                show_protagonist = info["show_protagonist"], 
                show_poster = info["show_poster"]
            )
            
            show.save()

            return render(request, "App_critik/shows/new_show.html")
        
    else:
            form_2 = add_show_form()

    return render (request, "App_critik/shows/add_show.html", {"form_2":form_2})

def shows(request):
    show_catalogue = new_show.objects.all()
    return render(request, "App_critik/shows/all_shows.html", {"show_catalogue": show_catalogue})

def view_show(request, show_id):
    selected_show = get_object_or_404(new_show, pk = show_id)

    return render(request, "App_critik/shows/show.html", {"selected_show":selected_show})

def show_review(request):
    if request.method == "POST":

        form_3 = new_show_review_form(request.POST)

        if form_3.is_valid():

            info = form_3.cleaned_data

            show_review = new_show_review_form(
                show_score = info["show_core"],
                show_favorite_character = info["show_favorite_character"], 
                show_review = info["show_review"], 
            )
            
            show_review.save()

            return render(request, "App_critik/shows/all_shows.html")
        
    else:
            form_3 = new_show_review_form()

    return render (request, "App_critik/shows/new_review.html", {"form_3":form_3})


def about(request):
    pass


# LOGIN / PERFIL 
def profile(requiest):
    pass

def login(request):
    
    if request.method == "POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            
            user = authenticate(username = usuario, password = contraseña)
            
            if user:
                
                login(request, user)
                
                return render(request, "url")
            
        else:
            
            return render(request, "url", {"mensaje": "Datos incorrectos"})
        
    else:
        
        form = AuthenticationForm()
        
    return render(request, "login.html", {"form"})