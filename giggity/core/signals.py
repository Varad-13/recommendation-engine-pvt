from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from .models import UserProfile, Tag, UserInterests, Freelancer

@receiver(user_signed_up)
def user_signed_up_handler(sender, request, user, **kwargs):
    create_freelancer_profile(user)
    populate_user_interests(user)

def create_freelancer_profile(user):
    freelancer, created = Freelancer.objects.get_or_create(user=user)

def populate_user_interests(user):
    user_profile = UserProfile.objects.get(user=user)
    tags = Tag.objects.all()

    for tag in tags:
        user_interest, created = UserInterests.objects.get_or_create(user=user, tag=tag)
        user_interest.score = 0
        user_interest.save()
