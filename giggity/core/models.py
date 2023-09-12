from django.contrib.auth.models import AbstractUser
from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')

class UserProfile(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    profile_image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=255, unique=True)

class Freelancer(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    freelancer_id = models.AutoField(primary_key=True)
    custom_url = models.CharField(max_length=255, unique=True)
    rating = models.FloatField()
    paypal_id = models.CharField(max_length=255)

class Tag(models.Model):
    tag = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    images = models.ManyToManyField(Image)
    link = models.URLField()
    tags = models.ManyToManyField(Tag)

class Interaction(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
