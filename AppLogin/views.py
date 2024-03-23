from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import *
from django.contrib.auth import *
from AppLogin.models import *
from AppLogin.forms import *


# LOGIN

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



# SIGNUP

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



# EDIT USER
@login_required
def edit_user(request):
    
    usuario = request.user
    
    if request.method == "POST":
        
        form = EditUser(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data
            
            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            
            usuario.save()
            
            return render(request, "edit_complete.html")
    
    else:
        
        form = EditUser(initial={
           "email":usuario.email,
           "first_name":usuario.first_name, 
           "last_name":usuario.last_name
        })
        
    return render(request, "edit_user.html",{"formulario": form, "usuario":usuario}) 

def edit_complete(request):
    
    render(request, "edit_complete.html")      
    


# AVATAR
@login_required
def upload_avatar(request):

    if request.method == "POST":

        form = AvatarForm(request.POST,request.FILES)

        if form.is_valid():

            actualUser = User.objects.get(username=request.user)

            avatar = Avatar(user=actualUser, image = form.cleaned_data["image"])

            avatar.save()

            return render(request, "avatar_complete.html")

    else:

        form = AvatarForm()

    return render(request, "avatar.html", {"formulario":form})

def avatar_complete(request):

    return render(request, "avatar_complete.html")
