from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    second_name = models.CharField(max_length=123, default='None')
    age = models.PositiveSmallIntegerField(default=0)

    def get_full_name(self):
        return f'LastName: {self.last_name}, FirstName:{self.first_name}'
    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name}'

class Book(models.Model):
    author = models.CharField(max_length=128, default='Inkognito')
    title = models.CharField(max_length=128)

