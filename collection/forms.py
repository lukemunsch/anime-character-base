from django import forms
from .models import Character


class CreateCharacterForm(forms.ModelForm):
    """set up the form to process character creations"""
    class Meta:
        """what we expect our form to include"""
        model = Character
        fields = ('name','char_image', 'series_name', 'age', 'special', 'first_published', 'first_aired', 'good_reason', 'bad_reason', 'bio',)
