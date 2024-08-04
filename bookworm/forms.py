from django import forms
from django.contrib.auth.models import User
from .models import Book, Rating



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
        widgets = {'rating': forms.RadioSelect(choices=[(i, i) for i in range(1, 6)]),}