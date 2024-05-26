from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'image', 'author', 'published_date', 'ISBN']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }