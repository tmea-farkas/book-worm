from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books', views.new_book, name='book'),
    path('books/new-book', views.new_book, name='new-book'),
    path('books/add-post/', views.addPost, name='add-post'),


]