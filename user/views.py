from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from user.utill import generate_random_password
from user.forms import UserForm
from django.urls import reverse


from faker import Faker
from user.models import User
from user.models import Book
from user.forms import UserBooks
from user.models import User


# Create your views here.


def generate_password(request):
    length = int(request.GET.get('len'))
    result = generate_random_password(length)
    return HttpResponse(str(result))


def users(request):
    print('IP Address for debug-toolbar: ' + request.META['REMOTE_ADDR'])
    contex = {'user_list': User.objects.all()}
    return render(request, 'list_user.html', contex)


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid:
            form.save()
            #return HttpResponseRedirect(reverse('users-name'))
            return redirect('users-name')
    elif request.method == 'GET':
        form = UserForm()

    context = {'user_form': form}
    return render(request, 'create_user.html', context= context)


def update_user(request,pk):

    #try:
        #user = User.objects.get(pk=pk)
    #except User.DoesNotExist:
        #raise Http404
    user = get_object_or_404(User, pk=pk)


    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid:
            form.save()
            #return HttpResponseRedirect(reverse('users-name'))
            return redirect('users-name')
    elif request.method == 'GET':
        # instance == type(user) == User
        form = UserForm(instance=user)

    context = {'user_form': form, 'user_instance': user,}
    return render(request, 'create_user.html', context= context)


def all_books(request):
    # books = Book.objects.all()
    #results = ''
    #for book in books:
        #results += f'ID: {book.id}, Author: {book.author}, Title: {book.title}'
    #return HttpResponse(results)
    print('IP Address for debug-toolbar: ' + request.META['REMOTE_ADDR'])
    contex = {'book_list': Book.objects.all()}
    return render(request, 'book_list.html', contex)


def create_book(request):
    if request.method == 'POST':
        form = UserBooks(request.POST)
        if form.is_valid:
            form.save()
            #return HttpResponseRedirect('/books/list/')
            return redirect('book-list')
    elif request.method == 'GET':
        form = UserBooks()

    context = {'book_form': form}
    return render(request, 'create_book.html', context= context)

def update_books(request, pk):
    book = get_object_or_404(Book, pk=pk)


    if request.method == 'POST':
        form = UserBooks(request.POST, instance=book)
        if form.is_valid:
            form.save()
            #return HttpResponseRedirect('/books/list/')
            return redirect('book-list')
    elif request.method == 'GET':
        form = UserBooks(instance=book)

    context = {'book_form': form}
    return render(request, 'create_book.html', context= context)


def book_list(request):
    #fake = Faker()
    #title_book = Book.objects.create(title = fake.first_name(),
                                     #author = fake.name())
    #return HttpResponse(f'ID:{title_book.id}, Author: {title_book.author}, Title: {title_book.title}')
    form = UserBooks(request.POST)
    is_valid = form.is_valid()
    if is_valid:
        form.save()
    else:
        print(form.errors)
    context = {'book_form': form}
    return render(request, 'create_book.html', context= context)



def index(request):
    return render(request, 'index.html', )


