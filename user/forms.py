from django import forms
from user.models import User, Book


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class UserBooks(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('author', 'title')
