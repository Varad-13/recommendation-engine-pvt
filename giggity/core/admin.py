from django.contrib import admin

from .models import UserProfile, Freelancer, Tag, Interaction

admin.site.register(UserProfile)
admin.site.register(Freelancer)
admin.site.register(Tag)
admin.site.register(Interaction)
