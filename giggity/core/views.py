from django.shortcuts import render, redirect
from .models import UserProfile, Post, Post_tag, Recommendations

def landing(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return render(request, 'core/landing.html')


def index(request):
    if request.user.is_authenticated:
        users = UserProfile.objects.exclude(username=request.user.username)
        posts = Post.objects.all()
        user_profiles = UserProfile.objects.in_bulk([post.freelancer.user_id.id for post in posts])
        tags = Post_tag.objects.filter(post__in=posts).distinct()
        context = {
            'users': users,
            'posts' : posts,
            'user_profiles': user_profiles,
            'tags': tags,
        }
        return render(request, 'core/index.html', context)
    else:
        return redirect('landing')

def search(request, query):
    results = Post.objects.filter(name__contains=query)
    context = {
        'query' : query,
        'posts' : results,
    }
    return render(request, 'core/search.html', context)

def recommendations_view(request):
    user = request.user  # Assuming you're using authentication
    recommendations = Recommendations.objects.filter(user=user, visited=False).order_by('-score')[:9]
    recommended_posts = [recommendation.post for recommendation in recommendations]

    return render(request, 'core/for_you.html', {'posts': recommended_posts})

def top_posts_view(request):
    top_posts = Post.objects.all().order_by('-post_id')[:9]  # Adjust the ordering criteria as needed

    return render(request, 'core/top_posts.html', {'posts': top_posts})
