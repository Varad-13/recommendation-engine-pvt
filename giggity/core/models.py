from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

CATAGORY = (
    ('gig', 'gig'),
    ('project', 'project'),
)


class User(AbstractUser):
    pfp = models.ImageField(upload_to='pfps', null=True, blank=True, default='user-regular.svg')
    username = models.CharField(max_length=50, null=True)
    email = models.EmailField(unique=True, null=True)
    fname = models.CharField(max_length=20, null=True)
    lname = models.CharField(max_length=20, null=True)
    phone = models.BigIntegerField(null=True)
    naive = models.BooleanField(default=True)

    

    def _str_(self):
        return self.username

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

class Tags(models.Model):
    title = models.CharField(max_length=20)



class Images(models.Model):
    name = models.CharField(max_length=20)
    img = models.FileField(upload_to='imgs/')



class Service(models.Model):
    title = models.CharField(max_length=20)
    freelancer = models.ForeignKey(User, on_delete= models.CASCADE)
    desc = models.TextField()
    img = models.ManyToManyField(Images)
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    catagory = models.CharField(max_length = 50, choices = CATAGORY, default='gig')
    link = models.URLField()

# Create your models here.

class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length=20, blank=True)
    rating = models.FloatField()
    product = models.ForeignKey(Service, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

class Bookmark(models.Model):
    product = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

class Purchase(models.Model):
    product = models.ForeignKey(Service, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchase')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sell')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)
    transaction_id = models.CharField(max_length=20)