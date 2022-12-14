from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

class Book(models.Model):
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=128)

