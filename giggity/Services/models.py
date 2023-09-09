from django.db import models
from core.models import UserProfile, Freelancer, Image

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    images = models.ManyToManyField(Image)
    link = models.URLField()

class Service(models.Model):
    is_recurring = models.BooleanField()
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
