from django import forms
from user.models import User
from user.models import Book


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'age', 'phone')

    def save(self, commit=True):
        #forms.ModelForm.save(self, commit)
        user = super().save(commit=False)
        user.email = user.email.lower()
        user.first_name = user.first_name.title()
        user.last_name = user.last_name.title()
        user.phone = user.phone = user.phone.lower()
        user.save()
        return user


class UserBooks(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('author', 'title')
