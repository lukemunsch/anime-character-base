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


class TestSeries(TestCase):
    """set up tests for Series"""
    def create_ser(
        self,
        series_name="TEST",
        series_logo="placeholder"
        ):
        """create a series"""
        return Series.objects.create(
            series_name=series_name,
            series_logo=series_logo
            )

    def test_series_return_str(self):
        """testing for series returns"""
        s = self.create_ser()
        self.assertTrue(isinstance(s, Series))
        self.assertEqual(s.__str__(), s.series_name)

    def test_series_creation_view(self):
        """test if series creation is functioning"""
        form = AddSerForm({
            'series_name': 'test ser',
        })
        self.assertTrue(form.is_valid())
        form.save()


class TestCharacter(TestCase):
    """set up tests for character"""
    def create_c(
        self,
        name="test",
        slug="test",
        char_image="placeholder",
        series_name="test",
        first_published="2012-01-02",
        first_aired="2012-01-02",
        age="23",
        bio="testing bio",
        special="test special",
        good_reason="test good",
        bad_reason="test bad",
        created_on="2022-02-22",
        updated_on="2022-02-22",
        status=1
        ):
        """creation of a character"""
        return Character.objects.create(
            name=name,
            slug=slug,
            char_image=char_image,
            series_name=series_name,
            first_aired=first_aired,
            first_published=first_published,
            age=age,
            bio=bio,
            special=special,
            good_reason=good_reason,
            bad_reason=bad_reason,
            created_on=created_on,
            updated_on=updated_on,
            status=status
        )

    def test_character_return_str(self):
        """test for character creation"""
        series = Series(series_name="test")
        series.save()
        c = self.create_c(series_name=series)
        self.assertTrue(isinstance(c, Character))
        self.assertEqual(c.__str__(), c.name)

    def test_create_char_view(self):
        """test for our create character"""
        series = Series(series_name="test")
        series.save()
        form = CreateCharForm({
            'name': 'test',
            'slug': 'test',
            'char_image': 'image',
            'series_name': series,
            'first_aired': '2022-02-22',
            'first_published': '2022-02-22',
            'age': '22',
            'bio': "test bio",
            'special': 'test spec',
            'good_reason': 'good test',
            'bad_reason': 'bad test',
            'created_on': '2022-02-22',
            'updated_on': '2022-02-22',
            'status': '1'
        })
        self.assertTrue(form.is_valid())

    def test_edit_character_view(self):
        """testing our editing function view for character"""


class TestComment(TestCase):
    """set up the tests for Comments"""
    def create_com(
        self,
        character="test",
        name="joe",
        body="test body",
        created_on="2022-02-22",
        ):
        """creating instance of comm"""
        return Comment.objects.create(
            character=character,
            name=name,
            body=body,
            created_on=created_on
            )
    
    def test_comment_return_str(self):
        """create a comment"""
        series = Series(series_name="Test")
        series.save()
        character = Character(name="Test", series_name=series)
        character.save()
        c = self.create_com(character=character)
        self.assertTrue(isinstance(c, Comment))
        self.assertEqual(c.__str__(), c.name)


class TestSuggestion(TestCase):
    """tests for suggestions"""
    def create_sug(
        self,
        sug_type=1,
        char_sug="nothing",
        series_sug="test",
        reason="test reason",
        created_when="2022-02-22"
    ):
        """crete a suggestion"""
        return Suggestion.objects.create(
            sug_type=sug_type,
            char_sug=char_sug,
            series_sug=series_sug,
            reason=reason,
            created_when=created_when
        )

    def test_suggestion_return_str(self):
        """test our creation"""
        s = self.create_sug()
        self.assertTrue(s, Suggestion)
        self.assertEqual(s.__str__(), s.reason)
