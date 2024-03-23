from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import User

# FORMS DE PELICULAS

class add_movie_form(forms.Form):
    movie_name = forms.CharField(label = 'Nombre de la película', max_length = 60)
    movie_release_year = forms.IntegerField(label = 'Año de estreno')
    movie_genre = forms.CharField(label = 'Género', max_length = 40)
    movie_director = forms.CharField(label = 'Director/es', max_length = 40)
    movie_protagonist = forms.CharField(max_length = 40)
    movie_poster = forms.ImageField(label = 'Poster', required = False)

class new_movie_review_form(forms.Form):
    movie_score = forms.IntegerField(label="Puntaje")
    movie_favorite_character = forms.CharField(label="Personaje favorito", max_length = 40)
    movie_review = forms.CharField(label="Opinión", max_length = 300)


# FORMS DE SERIES

class add_show_form(forms.Form):
    show_name = forms.CharField(label = "Nombre de la serie", max_length = 60)
    show_release_year = forms.IntegerField(label = "Año de estreno")
    show_genre = forms.CharField(label = "Género",max_length = 40)
    show_director = forms.CharField(label = "Director/es",max_length = 40)
    show_protagonist = forms.CharField(max_length = 40)
    show_poster = forms.ImageField(label = "Poster", required = False)

class new_show_review_form(forms.Form):
    show_score = forms.IntegerField(label="Puntaje")
    show_favorite_character = forms.CharField(label="Personaje favorito",max_length = 40)
    show_review = forms.CharField(label="Opinión",max_length = 300)