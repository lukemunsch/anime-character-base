from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Series, Character, Comment, Suggestion


@admin.register(Character)
class CharacterAdmin(SummernoteModelAdmin):
    """set up for our character creation form"""
    prepopulated_fields = {'slug': ('name',)}
    summernote_field = ['bio']

    list_filter = ('status',)
    list_display = (
        'name',
        'series_name',
        'first_published',
        'first_aired',
        'status',
        )
    search_fields = [
        'name',
        'series_name',
        'bio',
        'good_reason',
        'bad_reason'
        ]


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    """set up admin page for Series"""
    list_display = ('series_name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """set up our admin page for Comments"""
    list_display = ('name', 'character', 'created_on',)
    search_fields = ['character', 'name', 'email', 'body']


@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    """setting up my Suggestion admin to montior creation progress"""
    list_display = ('sug_type', 'char_sug', 'series_sug', 'created_when',)
    list_filter = ('sug_type',)
    search_fields = ['series_sug', 'char_sug']
