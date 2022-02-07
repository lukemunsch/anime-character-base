"""Set up the view for our models"""
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django import forms
from django.views import generic, View
from .models import Character, Series, Comment
from .forms import CreateCharacterForm


class CharacterList(generic.ListView):
    """this is the display of our Character model"""
    model = Character
    queryset = Character.objects.filter(status=1).order_by('-series_name')
    template_name = 'index.html'
    paginate_by = 8


class SeriesList(generic.ListView):
    """This is to display the list of series I have added to my db"""
    model = Series
    queryset = Series.objects.filter(approved=1).order_by('series_name')
    template_name = 'series_list.html'
    paginate_by = 10


class CharacterDetail(View):
    """creating he view for our character's main pages"""
    def get(self, request, slug, *args, **kwargs):
        """retrieving from the database"""
        queryset = Character.objects.filter(status=1)
        character = get_object_or_404(queryset, slug=slug)
        

        return render(
            request,
            "character_detail.html",
            {
                "character": character,
                "commented": False,
            },
        )


class CreateCharacter(View):
    """set up the request for posting a new character"""
    def create_char(self, request):
        """if the request is a post, populate the data from the request"""
        if request.method == 'POST':
            char_form = CreateCharacterForm(request.POST)
            if char_form.is_valid():
                char_form.save()
                return redirect('create_char')
        char_form = CreateCharacterForm()
        context = {
            'char_form': char_form
        }
        return render(request, 'create_character.html', context)
