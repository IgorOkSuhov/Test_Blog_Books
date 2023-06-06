from celery import shared_task
from django.core.mail import send_mail

from user.utill import smth_slow

@shared_task
def smth_slow_async(wait=10):
    print('1'*100)
    smth_slow(wait)

@shared_task
def send_email_async(subject, text):
    send_mail(
            subject,
            text,
            'from@example.com',
            ['igoroksuhov060195@gmail.com'],
            fail_silently=False,
        )

