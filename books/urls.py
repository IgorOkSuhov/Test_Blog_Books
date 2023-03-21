"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from user import views as uv

from django.contrib import admin
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('gp/', uv.generate_password),
    path('users/', uv.users),
    path('newusers/', uv.create_user),
    path('newbook/', uv.create_book),
    path('books/list/', uv.all_books),
    path('books/create/', uv.book_list),
    path('update_user/<int:pk>/', uv.update_user),
    path('update_books/<int:pk>/', uv.update_books),
]
