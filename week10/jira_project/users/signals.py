from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User, Profile


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.send_greeting_email()
        instance.send_activate_sms()
    print(instance)