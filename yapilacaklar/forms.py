from django import forms
from .models import *


class AddToDo(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('title', 'description', 'image', 'category', 'sub_category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description...'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'sub_category': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }