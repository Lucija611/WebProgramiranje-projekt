from django import forms
from .models import Note, Review


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'course_name', 'faculty', 'description', 'file']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }