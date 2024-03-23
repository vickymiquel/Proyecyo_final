from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import User

class UserRegister(UserCreationForm):
    
    username = forms.CharField(label = "Nombre de Usuario")
    email = forms.EmailField()
    fav_movie = forms.CharField(label = "Pelicula Favorita")
    fav_genre = forms.CharField(label = "Genero Favorito")
    password1 = forms.CharField(label="Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label=" Confirmar Contraseña", widget = forms.PasswordInput)
    
    class Meta:
        
        model = User
        fields = ["username", "email", "password1", "password2"]
        
class EditUser(UserCreationForm):
    
    email = forms.EmailField()
    fav_movie = forms.CharField(label = "Pelicula Favorita", required=False)
    fav_genre = forms.CharField(label = "Genero Favorito", required=False)
    password1 = forms.CharField(label="Contraseña", widget = forms.PasswordInput, required=False)
    password2 = forms.CharField(label=" Confirmar Contraseña", widget = forms.PasswordInput, required=False)
    
    class Meta:
        
        model = User
        fields = ["email", "password1", "password2"]