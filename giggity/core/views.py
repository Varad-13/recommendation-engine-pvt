from django.shortcuts import render
from .models import UserProfile, Post

def index(request):
    
    return render(request, 'core/landing.html')

def loggedin(request):
    users = UserProfile.objects.exclude(username=request.user.username)
    posts = Post.objects.all()
    context = {
        'users': users,
        'posts' : posts,
        
    }
    return render(request, 'core/index.html', context)