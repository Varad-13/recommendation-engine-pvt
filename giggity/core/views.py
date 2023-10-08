from django.shortcuts import render

def index(request):
    return render(request, 'core/landing.html')

def loggedin(request):
    return render(request, 'core/index.html')