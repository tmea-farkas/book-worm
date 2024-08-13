from django import forms
#from django.contrib.auth.models import User
from .models import Book, Rating, Genre



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'description', 'cover_photo']
        genre = forms.ModelChoiceField(
            queryset=Genre.objects.all(),
            widget=forms.Select,
            empty_label="Select a Genre"
            )
        
        def __init__(self):
            super(BookForm, self)

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
        widgets = {'rating': forms.RadioSelect(choices=[(i, i) for i in range(1, 6)]),}
