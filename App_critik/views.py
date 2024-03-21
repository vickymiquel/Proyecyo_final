from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import *
from django.contrib.auth import *
from App_critik.models import *
from App_critik.forms import *

def home(request):
    return render(request, "App_critik/home.html")

def movies(request):
    return render(request, "App_critik/movies.html")

def shows(request):
    return render(request, "App_critik/shows.html")

def about(request):
    pass

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