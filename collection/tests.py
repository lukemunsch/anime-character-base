"""Set up our imports to use in tests"""
from django.test import TestCase
from django.http import Http404
from django.shortcuts import get_object_or_404
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
    def test_get_series_list(self):
        """test to see if we can retrieve character list"""
        response = self.client.get('/series_list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'series_list.html')

    def test_series_return_str(self):
        """testing for series returns"""
        series = Series.objects.create(
                series_name='series_name',
                series_logo='series_logo'
                )
        self.assertEqual(series.__str__(), series.series_name)

    def test_series_creation_page(self):
        """test if series creation is functioning"""
        response = self.client.get('/create_series/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_series.html')

    def test_form_for_create_series_is_valid(self):
        """make sure series_name has a value"""
        series = AddSerForm({'series_name': ""})
        self.assertFalse(series.is_valid())
        self.assertIn('series_name', series.errors.keys())
        self.assertEqual(
            series.errors['series_name'][0],
            'This field is required.'
        )

    def test_create_series_form_redirects(self):
        """test for if series form saves"""
        response = self.client.post(
            '/create_series/',
            {'series_name': 'Test Series'}
        )
        self.assertRedirects(response, '/series_list/')

    def test_get_edit_series_page(self):
        """test for bringing up correct series edit page"""
        series = Series.objects.create(series_name='Test series')
        response = self.client.get(f'/edit_series/{series.id}')
        self.assertEqual(response.status_code, 301)

    def test_can_edit_series_object(self):
        """test proves series obj can be edited"""
        series = Series.objects.create(series_name='Test series')
        response = self.client.get(
            f'/edit_series/{series.id}'
        )
        self.assertEqual(response.status_code, 301)
        resp = self.client.post(
            f'/edit_series/{series.id}',
            {'series_name': 'updtestser'}
        )
        self.assertEqual(resp.status_code, 301)
        edited_series = Series.objects.get(id=series.id)
        self.assertTrue(edited_series.series_name, 'updtestser')

    def test_can_get_delete_series_page(self):
        """test to make sure an item can be deleted"""
        series = Series.objects.create(series_name='testser')
        response = self.client.post(f'/delete_series/{series.id}')
        self.assertEqual(response.status_code, 301)
        with self.assertRaises(Http404):
            get_object_or_404(Series, id=2)
        self.assertTemplateUsed('/delete_series.html')
        resp = self.client.get(f'/delete_series/{series.id}')
        with self.assertRaises(Http404):
            get_object_or_404(Series, id=2)
        existing_ser = Suggestion.objects.filter(id=series.id)
        self.assertEqual(len(existing_ser), 0)


class TestCharacter(TestCase):
    """set up tests for character"""
    def test_get_series_list(self):
        """test to see if we can retrieve character list"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_character_return_str(self):
        """test for character creation"""
        series = Series.objects.create(series_name='test')
        series.save()
        character = Character.objects.create(name='tester', series_name=series)
        self.assertEqual(character.__str__(), character.name)

    def test_character_creation_page(self):
        """test if character creation is functioning"""
        response = self.client.get('/create_character/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_character.html')

    def test_form_for_create_character(self):
        """make sure name has a value"""
        char = CreateCharForm({'name': ""})
        self.assertFalse(char.is_valid())
        self.assertIn('name', char.errors.keys())
        self.assertEqual(
            char.errors['name'][0],
            'This field is required.'
        )

    def test_create_character_form_save(self):
        """test for if character form saves"""
        response = self.client.post(
            '/create_character/',
            {
                'name': 'Test Series',
                'series_name': 'series test'
            }
        )
        self.assertRedirects(response, '/')

    def test_slugify_automatically_generates_slug(self):
        """test if slug is generated automatically with series_name-name"""
        series = Series.objects.create(series_name="testser")
        series.save()
        char = Character.objects.create(name='Test Char', series_name=series)
        char.save()
        self.assertEqual(char.slug, 'testser-test-char')

    def test_get_edit_character_page(self):
        """test for bringing up correct series edit page"""
        series = Series.objects.create(series_name="testser")
        series.save()
        char = Character.objects.create(
            name='Test',
            series_name=series
        )
        response = self.client.get(f'/edit_char/{char.slug}')
        self.assertEqual(response.status_code, 301)

    def test_can_view_character_details(self):
        """test to open specific character"""
        series = Series.objects.create(series_name='testser')
        series.save()
        character = Character.objects.create(name="test", series_name=series)
        character.save()
        response = self.client.get(f'/{character.slug}/')
        self.assertEqual(response.status_code, 200)


class TestComment(TestCase):
    """set up the tests for Comments"""
    def test_comment_return_str(self):
        """create a comment"""
        series = Series(series_name="Test")
        series.save()
        character = Character(name="Test", series_name=series)
        character.save()
        com = Comment.objects.create(character=character, name='test')
        self.assertEqual(com.__str__(), com.name)


class TestSuggestion(TestCase):
    """tests for suggestions"""
    def test_suggestion_return_str(self):
        """test our creation"""
        sug = Suggestion.objects.create(sug_type=1, reason="test reason")
        self.assertEqual(sug.__str__(), sug.reason)

    def test_get_suggestion_list(self):
        """test to display our sugestions"""
        response = self.client.get('/suggestions/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'suggestions.html')

    def test_get_add_suggestions_page(self):
        """test to bring up our create suggestions page"""
        response = self.client.get('/create_suggestion/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_suggestion.html')

    def test_can_add_item(self):
        """test to see if we can add a suggestion"""
        response = self.client.post(
            '/create_suggestion/',
            {
                'sug_type': 1,
                'reason': 'test reason'
            }
        )
        self.assertRedirects(response, '/suggestions/')

    def test_delete_sug_get_obj_or_404(self):
        """test to make sure invalid suggestions bring up 404"""
        sug = Suggestion.objects.create(sug_type=1)
        response = self.client.get(f'/delete_sug/{sug.id}/')
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Http404):
            get_object_or_404(Suggestion, id=2)
        existing_sug = Suggestion.objects.filter(id=sug.id)
        self.assertEqual(len(existing_sug), 0)
