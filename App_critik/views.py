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

