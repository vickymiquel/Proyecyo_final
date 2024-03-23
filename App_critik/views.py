from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import *
from django.contrib.auth import *
from App_critik.models import *
from App_critik.forms import *
from django.views.generic.edit import *

def home(request):
    return render(request, "App_critik/home.html")

# PELICULAS
def add_movie(request):

    if request.method == "POST":

        form_1 = add_movie_form(request.POST, request.FILES)

        if form_1.is_valid():

            info = form_1.cleaned_data

            movie = new_movie(
                usuario=request.user,
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

def search_movie(request):
    return render(request, "App_critik/shows/all_movies.html")

def search_movie_results(request):
    
    if request.GET["pelicula"]:

        pelicula = request.GET["pelicula"]

        available_movies = new_movie.objects.all()

        searched_movie = available_movies.filter(movie_name__icontains = pelicula)     

        return render(request, "App_critik/movies/search_movie_results.html", {"searched_movie":searched_movie, "pelicula":pelicula})

    else:
        result = "No enviaste datos"

    return HttpResponse(result)


def view_movie(request, movie_id):
    selected_movie = get_object_or_404(new_movie, pk = movie_id)

    return render(request, "App_critik/movies/movie.html", {"selected_movie":selected_movie})

def delete_movie(request, Movie_name):
    
    movie = new_movie.objects.get(movie_name = Movie_name)
    movie.delete()
    
    
    return render(request, "App_critik/movies/delete_complete.html")

def delete_complete_movie(request):
    
    return render(request, "App_critik/movies/delete_complete.html")

def update_movie(request, Movie_name):
    
    movie = new_movie.objects.get(movie_name = Movie_name)
    
    if request.method == "POST":
    
        form_1 = add_movie_form(request.POST, request.FILES)

        if form_1.is_valid():

                info = form_1.cleaned_data

                movie.movie_name = info["movie_name"]
                movie.movie_release_year = info["movie_release_year"]
                movie.movie_genre = info["movie_genre"]
                movie.movie_director = info["movie_director"]
                movie.movie_protagonist = info["movie_protagonist"]
                movie.movie_poster= info["movie_poster"]

                movie.save()

                return (request, "App_critik/movies/all_movies.html")
        
    else:
        
        form_1 = add_movie_form(initial={"movie_name":movie.movie_name, 
                                         "movie_release_year":movie.movie_release_year, 
                                         "movie_genre":movie.movie_genre,
                                         "movie_director":movie.movie_director,
                                         "movie_protagonist":movie.movie_protagonist,
                                         "movie_poster":movie.movie_poster
                                         })

    return render(request, "App_critik/movies/edit_movie.html", {"form_1":form_1, "movie_name": Movie_name})

# SERIES
def add_show(request):

    if request.method == "POST":

        form_2 = add_show_form(request.POST, request.FILES)

        if form_2.is_valid():

            info = form_2.cleaned_data

            show = new_show(
                usuario=request.user,
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

def search_show(request):
    return render(request, "App_critik/shows/all_shows.html")

def search_show_results(request):
    
    if request.GET["serie"]:

        serie = request.GET["serie"]

        available_shows = new_show.objects.all()

        searched_show = available_shows.filter(show_name__icontains = serie)



        return render(request, "App_critik/shows/search_show_results.html", {"searched_show":searched_show, "serie":serie})

    else:
        result = "No enviaste datos"

    return HttpResponse(result)

def view_show(request, show_id):
    selected_show = get_object_or_404(new_show, pk = show_id)
    return render(request, "App_critik/shows/show.html", {"selected_show":selected_show})

def delete_show(request, Show_name):
    
    show = new_show.objects.get(show_name = Show_name)
    show.delete()
    
    
    return render(request, "App_critik/shows/delete_complete.html")

def delete_complete_show(request):
    
    return render(request, "App_critik/shows/delete_complete.html")

def update_show(request, Show_name):
    
    show = new_show.objects.get(show_name = Show_name)
    
    if request.method == "POST":
    
        form_1 = add_show_form(request.POST, request.FILES)

        if form_1.is_valid():

                info = form_1.cleaned_data

                show.show_name = info["show_name"]
                show.show_release_year = info["show_release_year"]
                show.show_genre = info["show_genre"]
                show.show_director = info["show_director"]
                show.show_protagonist = info["show_protagonist"]
                show.show_poster= info["show_poster"]

                show.save()

                return (request, "App_critik/shows/all_shows.html")
        
    else:
        
        form_1 = add_show_form(initial={"show_name":show.show_name, 
                                         "show_release_year":show.show_release_year, 
                                         "show_genre":show.show_genre,
                                         "show_director":show.show_director,
                                         "show_protagonist":show.show_protagonist,
                                         "show_poster":show.show_poster
                                         })

    return render(request, "App_critik/shows/edit_show.html", {"form_1":form_1, "show_name": Show_name})

def show_review(request):
    if request.method == "POST":

        form_3 = new_show_review_form(request.POST)

        if form_3.is_valid():

            info = form_3.cleaned_data

            review_show = new_show_review(
                show_score = info["show_score"],
                favorite_show_character = info["show_favorite_character"], 
                show_review = info["show_review"], 
            )
            
            review_show.save()

            return render(request, "App_critik/shows/all_shows.html")
        
    else:
            form_3 = new_show_review_form()

    return render (request, "App_critik/shows/new_review.html", {"form_3":form_3})

def about(request):
    return render(request, "App_critik/aboutus.html")

