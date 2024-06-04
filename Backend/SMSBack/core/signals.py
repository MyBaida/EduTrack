from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import User

@receiver(pre_save, sender=User)
def update_user_username(sender, instance, **kwargs):
    if instance.email and instance.username != instance.email:
        instance.username = instance.email
        print('Username updated to email')
