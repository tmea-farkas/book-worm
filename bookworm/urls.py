from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.new_book, name='book'),
    path('books/new/', views.new_book, name='new-book'),
    path('top-10/', views.top_10, name='top-10'),
    path('genres/', views.genres, name='genres'),
    path('contact/', views.contact, name='contact')


]