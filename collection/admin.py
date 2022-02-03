from django.contrib import admin
from .models import Series, Character, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Character)
class CharacterAdmin(SummernoteModelAdmin):

    summernote_field = ['bio']

admin.site.register(Series)


admin.site.register(Comment)
