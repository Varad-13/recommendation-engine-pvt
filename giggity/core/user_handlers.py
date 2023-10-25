from django.shortcuts import get_object_or_404
from core.models import UserProfile, Tag, UserInterests, Freelancer  # Import models inside the functions

def create_freelancer_profile(user):
    # Create a Freelancer instance for the given user
    freelancer, created = Freelancer.objects.get_or_create(user=user)

def populate_user_interests(user):
    # Get the user profile
    user_profile = get_object_or_404(UserProfile, user=user)
   
    # Get all tags
    tags = Tag.objects.all()

    # Create or update user interests for each tag
    for tag in tags:
        user_interest, created = UserInterests.objects.get_or_create(user=user, tag=tag)
        user_interest.score = 0
        user_interest.save()
