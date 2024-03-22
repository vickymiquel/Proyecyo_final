from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import *
from django.contrib.auth import *
from AppLogin.models import *
from AppLogin.forms import *

def login(request):
    
    if request.method == "POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            
            user = authenticate(username = usuario, password = contraseña)
            
            if user:
                
                login(request, user)
                
                return render(request, "App_critik/home.html", {"bienvenida": f"Bienvenido/a {user}"})
            
        else:
            
            return render(request, "login_error.html", {"formulario":form, "mensaje": "Datos incorrectos, intente nuevamente"})
        
    else:
        
        form = AuthenticationForm()
        
    return render(request, "login.html", {"formulario":form})

def signup(request):
    
    if request.method == "POST":
        
        form = UserRegister(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "App_critik/home.html", {"bienvenida": "Se ha registrado su usuario correctamente"})
        
    else:
        
        form = UserRegister()
        
    return render(request, "signup.html", {"formulario":form})
    
    
 