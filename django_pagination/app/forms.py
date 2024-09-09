from django import forms
from .models import Book


class CreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','discription','author','published_year','price','genre']
