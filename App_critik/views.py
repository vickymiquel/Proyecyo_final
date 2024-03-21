from django.shortcuts import render

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