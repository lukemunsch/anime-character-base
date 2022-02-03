from django.contrib import admin
from .models import Series, Character, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Character)
class CharacterAdmin(SummernoteModelAdmin):
    """set up for our character creation form"""
    prepopulated_fields = {'slug': ('name',)}
    summernote_field = ['bio']

    list_filter = ('status',)
    list_display = ('name', 'series_name', 'first_published', 'first_aired', 'status',)
    search_fields = ['name', 'series_name', 'bio', 'good_reason', 'bad_reason']


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    """set up admin page for Series"""
    list_display = ('series_name', 'approved',)
    list_filter = ('approved',)
    actions = ['approve_series']

    def approve_series(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """set up our admin page for Comments"""
    list_display = ('name', 'character', 'created_on', 'approved')
    list_filter = ('approved',)
    search_fields = ['character', 'name', 'email', 'body']
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(approved=True)
