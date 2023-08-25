from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    profile_image = models.ForeignKey('Image', on_delete=models.SET_NULL, null=True)
    freelancer = models.ForeignKey('Freelancer', on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=255, unique=True)

class Freelancer(models.Model):
    freelancer_id = models.AutoField(primary_key=True)
    custom_url = models.CharField(max_length=255, unique=True)
    rating = models.FloatField()
    paypal_id = models.CharField(max_length=255)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')

class Tag(models.Model):
    tag = models.CharField(max_length=255)

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

class Interaction(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    service = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
