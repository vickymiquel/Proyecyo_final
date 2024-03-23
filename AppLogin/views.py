from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import *
from django.contrib.auth import *
from AppLogin.models import *
from AppLogin.forms import *

def login_view(request):
    
    if request.method == "POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            
            user = authenticate(username = usuario, password = contraseña)
            
            if user:
                
                login(request, user)
                
                return render(request, "login_complete.html", {"bienvenida": f"Bienvenido/a {user}"})
            
        else:
            
            return render(request, "login_error.html", {"formulario":form, "mensaje": "Datos incorrectos, intente nuevamente"})
        
    else:
        
        form = AuthenticationForm()
        
    return render(request, "login.html", {"formulario":form})

def login_complete(request):
    
    return render(request, "login_complete.html")

def signup(request):
    
    if request.method == "POST":
        
        form = UserRegister(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "signup_complete.html", {"bienvenida": "Se ha registrado su usuario correctamente"})
        
    else:
        
        form = UserRegister()
        
    return render(request, "signup.html", {"formulario":form})

def signup_complete(request):
    
    return render(request, "signup_complete.html")

@login_required
def edit_user(request):
    
    usuario = request.user
    
    if request.method == "POST":
        
        form = EditUser(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data
            
            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.fav_movie = info["fav_movie"]
            usuario.fav_genre = info["fav_genre"]
            
            usuario.save()
            
            return render(request, "edit_complete.html")
    
    else:
        
        form = EditUser(initial={
           "email":usuario.email,
        })
        
    return render(request, "edit_user.html",{"formulario": form, "usuario":usuario}) 

def edit_complete(request):
    
    render(request, "edit_complete.html")      
    
 