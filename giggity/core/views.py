from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from .models import UserProfile, Post, Post_tag, Recommendations, Interaction, Logs
from .forms import PostForm

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
        tags = Post_tag.objects.filter(post__in=posts, score__gt=0).distinct()
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
    results = Post.objects.filter(Q(name__contains=query) | Q(description__contains=query))
    context = {
        'query' : query,
        'posts' : results,
    }
    return render(request, 'core/search.html', context)

def recommendations_view(request):
    user = request.user
    if user.is_authenticated:
        recommendations = Recommendations.objects.filter(user=user, visited=False).order_by('-score')[:9]
        recommended_posts = [recommendation.post for recommendation in recommendations]

        return render(request, 'core/for_you.html', {'posts': recommended_posts})
    else:
        return redirect('index')

def top_posts_view(request):
    top_posts = Post.objects.all().order_by('-post_id')[:9]  # Adjust the ordering criteria as needed

    return render(request, 'core/top_posts.html', {'posts': top_posts})


def create_post(request):
    error = None
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if not request.FILES.get('images'):
            error = "Image is a required field!"
        if form.is_valid():
            post = form.save(commit=False)
            freelancer = Freelancer.objects.get(user_id=request.user)
            post.freelancer = freelancer
            post.link = slugify(post.name.replace(" ", "-")) 
            post.save()
            populate_post_tags(post.link)
            return redirect('post_details', post.link)
    else:
        form = PostForm()
    return render(request, 'core/create_post.html', {'form': form, 'error':error})

def post_details(request, link):
    post = get_object_or_404(Post, link=link)
    tags = Post_tag.objects.filter(post__in=posts, score__gt=0).distinct()
    if not tags and post.freelancer.userid == request.user:
        print(".") #Temporary response. TODO: Redirect to a page where tags can be added
    context={
        'post' : post
    }
    if request.user.is_authenticated:
        user = request.user
        interaction = Interaction(
            user=user,
            post=post,
            action="click",
        )
        interaction.save()
        log = Logs(
            user=user,
            post=post,
            action="click",
        )
        log.save()
    return render(request, 'core/details.html', context)


# Automated tasks

def populate_post_tags(link):
    # Get all posts and tags
    post = get_object_or_404(Post, link=link)
    tags = Tag.objects.all()

    # Loop through each tag, creating Post_tag instances with a score of 0
    for tag in tags:
        post_tag, created = Post_tag.objects.get_or_create(post=post, tag=tag)
        post_tag.score = 0
        post_tag.save()