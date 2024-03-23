from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from AppLogin.models import *


# REGISTRO
class UserRegister(UserCreationForm):
    
    username = forms.CharField(label = "Nombre de Usuario")
    email = forms.EmailField()
    first_name = forms.CharField(label = "Nombre")
    last_name = forms.CharField(label = "Apellido")
    password1 = forms.CharField(label="Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label=" Confirmar Contraseña", widget = forms.PasswordInput)
    
    class Meta:
        
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]


 
class EditUser(UserCreationForm):
   
    email = forms.EmailField()
    first_name = forms.CharField(label = "Nombre")
    last_name = forms.CharField(label = "Apellido")
    password1 = forms.CharField(label="Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label=" Confirmar Contraseña", widget = forms.PasswordInput)
    
    class Meta:
        
        model = User
        fields = ["email", "password1", "password2","first_name", "last_name"]

class AvatarForm(forms.ModelForm):

    class Meta:

        model = Avatar
        fields = ["image"]

#