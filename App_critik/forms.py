from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from .models import *

# FORMS DE PELICULAS

class add_movie_form(forms.Form):
    movie_name = forms.CharField(label = 'Nombre de la película', max_length = 60)
    movie_release_year = forms.IntegerField(label = 'Año de estreno')
    movie_genre = forms.CharField(label = 'Género', max_length = 40)
    movie_director = forms.CharField(label = 'Director/es', max_length = 40)
    movie_protagonist = forms.CharField(label = "Protagonista", max_length = 40)
    movie_poster = forms.ImageField(label = 'Poster', required = False)

class new_movie_review_form(forms.ModelForm):
    class Meta:
        model = new_movie_review
        fields = ['movie_score', 'favorite_movie_character', 'movie_review', 'movie']


# FORMS DE SERIES

class add_show_form(forms.Form):
    show_name = forms.CharField(label = "Nombre de la serie", max_length = 60)
    show_release_year = forms.IntegerField(label = "Año de estreno")
    show_genre = forms.CharField(label = "Género",max_length = 40)
    show_director = forms.CharField(label = "Director/es",max_length = 40)
    show_protagonist = forms.CharField(label = "Protagonista", max_length = 40)
    show_poster = forms.ImageField(label = "Poster", required = False)

class new_show_review_form(forms.ModelForm):
    class Meta:
        model = new_show_review
        fields = ['show_score', 'favorite_show_character', 'show_review', 'show']