from django.apps import AppConfig
from allauth.account.signals import user_signed_up
from django.db.models.signals import connect  # Corrected import statement
from core.user_handlers import create_freelancer_profile, populate_user_interests

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        user_signed_up.connect(create_freelancer_profile, sender=self)
        user_signed_up.connect(populate_user_interests, sender=self)
