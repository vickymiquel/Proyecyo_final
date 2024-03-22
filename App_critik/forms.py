from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import User

class add_movie_form(forms.Form):
    movie_name = forms.CharField(label = 'Nombre de la película', max_length = 60)
    movie_release_year = forms.IntegerField(label = 'Año de estreno')
    movie_genre = forms.CharField(label = 'Género', max_length = 40)
    movie_director = forms.CharField(label = 'Director/es', max_length = 40)
    # movie_poster = forms.ImageField(label = 'Poster')


class add_show_form(forms.Form):
    show_name = forms.CharField(label = "Nombre de la serie", max_length = 60)
    show_year_release = forms.IntegerField(label = "Año de estreno")
    show_director = forms.CharField(label = "Director/es",max_length = 40)
    show_genre = forms.CharField(label = "Género",max_length = 40)
    # show_poster = forms.ImageField(label = "Poster")

class new_movie_review_form(forms.Form):
    Puntaje_de_la_pelicula = forms.IntegerField()
    Personaje_favorito = forms.CharField(max_length = 40)
    Opinion_de_la_pelicula = forms.CharField(max_length = 250)

class new_show_review_form(forms.Form):
    Puntaje_de_la_serie = forms.IntegerField()
    Personaje_favorito_serie = forms.CharField(max_length = 40)
    Opinion_de_la_serie = forms.CharField(max_length = 250)