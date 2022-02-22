from django import forms
from django.forms import (
    TextInput,
    FileInput,
    NumberInput,
    Select,
    DateInput,
    Textarea
    )
from .models import Character, Series, Suggestion, Comment


class CreateCharForm(forms.ModelForm):
    """set up the form to process character creations"""
    class Meta:
        """what we expect our form to include"""
        model = Character
        fields = [
            'name',
            'char_image',
            'series_name',
            'age',
            'special',
            'first_published',
            'first_aired',
            'good_reason',
            'bad_reason',
            'bio'
        ]
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control mb-4",
                'style': 'max-width: 400px;',
                'placeholder': 'Character Name'
                }),
            'char_image': FileInput(attrs={
                'class': "form-control mb-4",
                'style': 'max-width: 250px;',
            }),
            'series_name': Select(attrs={
                'class': "form-control mb-4",
                'style': 'max-width: 250px;',
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


class AddSerForm(forms.ModelForm):
    """setting up my form to add new series to the db"""
    class Meta:
        """what it will reference"""
        model = Series
        fields = ['series_name', 'series_logo']
        widgets = {
            'series_name': TextInput(attrs={
                'class': "form-control mb-4",
                'style': 'max-width: 250px;',
                'placeholder': 'Series Name'
                }),
            'series_logo': FileInput(attrs={
                'class': "form-control mb-4",
                'style': 'max-width: 250px;',
                'placeholder': 'Series Image'
                }),
        }


class CreateSugForm(forms.ModelForm):
    """create a form for people to send me suggestions"""
    class Meta:
        """how I would like the form to look"""
        model = Suggestion
        fields = ['sug_type', 'char_sug', 'series_sug', 'reason']
        widgets = {
            'sug_type': Select(attrs={
                'class': "form-control mb-4",
                'style': 'max-width: 250px;',
                'placeholder': 'Suggestion for a :'
            }),
            'char_sug': TextInput(attrs={
                'class': "form-control mb-4",
                'style': 'max-width: 250px;',
                'placeholder': 'Character Suggestion'
                }),
            'series_sug': TextInput(attrs={
                'class': "form-control mb-4",
                'style': 'max-width: 250px;',
                'placeholder': 'Series Suggestion'
                }),
            'reason': Textarea(attrs={
                'class': "form-control mb-4",
                'style': 'max-width: 500px;',
                'placeholder': 'Why would you recommend this?'
            }),
        }


class ComForm(forms.ModelForm):
    """how we expect our form to look"""
    class Meta:
        """what the form entails"""
        model = Comment
        fields = ('body',)
        widgets = {
            'body': Textarea(attrs={
                'class': "form-control mb-4",
                'style': 'max-width: 250px;',
                'placeholder': 'Please leave a review!'
            })
        }
