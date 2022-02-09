from django import forms
from .models import Character, Series, Suggestion
from django.forms import TextInput, FileInput, NumberInput, Select, DateInput, Textarea


class CreateCharacterForm(forms.ModelForm):
    """set up the form to process character creations"""
    class Meta:
        """what we expect our form to include"""
        model = Character
        fields = ['name', 'char_image', 'series_name', 'age', 'special', 'first_published', 'first_aired', 'good_reason', 'bad_reason', 'bio']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control mb-4",
                'style': 'max-width: 250px;',
                'placeholder': 'Character Name'
                }),
            'char_image': FileInput(attrs={
                'class': "form-control mb-4",
                'style': 'max-width: 250px;',
                'placeholder': 'Character Image'
            }),
            'series_name': Select(attrs={
                'class': "form-control mb-4",
                'style': 'max-width: 250px;',
                'placeholder': 'Series Name'
            }),
            'age': NumberInput(attrs={
                'class': "form-control mb-4",
                'style': 'max-width: 90px;',
                'placeholder': 'Series Name'
                }),
            'special': TextInput(attrs={
                'class': "form-control mb-4",
                'style': 'max-width: 500px;',
                'placeholder': 'Special Abilities'
                }),
            'first_published': DateInput(attrs={
                'class': "form-control mb-4",
                'style': 'max-width: 250px;',
                'placeholder': 'Published Date'
                }),
            'first_aired': DateInput(attrs={
                'class': "form-control mb-4",
                'style': 'max-width: 250px;',
                'placeholder': 'Published Date'
                }),
            'good_reason': TextInput(attrs={
                'class': "form-control mb-4",
                'style': 'max-width: 500px;',
                'placeholder': 'Positive Reason'
                }),
            'bad_reason': TextInput(attrs={
                'class': "form-control mb-4",
                'style': 'max-width: 500px;',
                'placeholder': 'Negative Reason'
                }),
            'bio': Textarea(attrs={
                'class': "form-control mb-4",
                'style': 'max-width: 500px;',
                'placeholder': 'Please Enter Your Biography Here'
            }),
        }
