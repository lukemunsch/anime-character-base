from django.test import TestCase
from .models import (
    Character,
    Series,
    Suggestion,
    Comment
)
from .forms import (
    CreateCharForm,
    CreateSugForm,
    AddSerForm,
    ComForm
)
from .views import (
    create_char,
    create_series,
    create_sug,
    edit_char,
    edit_series,
    delete_char,
    delete_comm,
    delete_series,
    delete_sug,
    CharacterList,
    CharDetail,
    SeriesList,
    SuggestionList,
)

# Create your tests here.
class TestModels(TestCase):
    """generic test"""
    def test_character_model(self):
        """set up tests for character model"""
        
