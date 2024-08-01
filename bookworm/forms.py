from django import forms
from django.contrib.auth.models import User
from .models import Profile, Rating



class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
        widgets = {'rating': forms.RadioSelect(choices=[(i, i) for i in range(1, 6)]),}