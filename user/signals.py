from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import re

from user.models import User


@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    if created:
        print('Created')
    else:
        print('No')

@receiver(pre_save, sender=User)
def user_pre_seve(sender, instance, *args, **kwargs):
    instance.email = instance.email.lower()
    instance.first_name = instance.first_name.title()
    instance.last_name = instance.last_name.title()
    instance.phone = instance.phone.lower()

    if not instance.phone.isdigit():
        instance.phone = re.sub("[^0-9]","",instance.phone)



