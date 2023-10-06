from django.db import models
from core.models import UserProfile, Freelancer, Post

class Service(models.Model):
    is_recurring = models.BooleanField()
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
