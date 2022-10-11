from django.shortcuts import render
from django.http import HttpResponse
from user.utill import generate_random_password

from faker import Faker
from user.models import User
from user.models import Book

# Create your views here.

def generate_password(request):
    length = int(request.GET.get('len'))
    result = generate_random_password(length)
    return HttpResponse(str(result))

def users(request):
    users = User.objects.all()
    results = ''
    for user in users:
        results += f'ID: {user.id}, Email: {user.email}'
    return HttpResponse(results)

def create_user(request):
    fake = Faker()
    user = User.objects.create(email = fake.email(),
                               first_name = fake.first_name(),
                               last_name = fake.last_name())

    return HttpResponse(f'ID: {user.id}, Email: {user.email}')


def all_books(request):
    books = Book.objects.all()
    results = ''
    for book in books:
        results += f'ID: {book.id}, Author: {book.author}, Title: {book.title}'
    return HttpResponse(results)



def book_list(request):
    fake = Faker()
    title_book = Book.objects.create(title = fake.first_name(),
                                     author = fake.name())

    return HttpResponse(f'ID:{title_book.id}, Author: {title_book.author}, Title: {title_book.title}')

