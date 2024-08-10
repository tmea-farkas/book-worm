from django.contrib import admin
from .models import Comment, Book, Rating, Genre
# Register your models here.
admin.site.register(Comment)
admin.site.register(Book)
admin.site.register(Genre)