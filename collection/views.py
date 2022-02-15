"""Set up the view for our models"""
from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponseRedirect
from django.views import generic, View
from .models import Character, Series, Comment, Suggestion
from .forms import CreateCharacterForm, CreateSeriesForm, CreateSuggestionForm


def create_char(request):
    """processing our create character to render a view"""
    if request.method == "POST":
        char_form = CreateCharacterForm(request.POST, request.FILES)
        if char_form.is_valid():
            char_form.save()
        return redirect(reverse('home'))
    char_form = CreateCharacterForm()
    context = {
        'char_form': char_form
    }
    return render(request, 'create_character.html', context)


def edit_char(request, slug):
    """process how to delete a character"""
    char = get_object_or_404(Character, slug=slug)
    if request.method == "POST":
        char_form = CreateCharacterForm(request.POST, request.FILES, instance=char)
        if char_form.is_valid():
            char_form.save()
            return redirect(reverse('home'))
    char_form = CreateCharacterForm(instance=char)
    context = {
        'char_form': char_form
    }
    return render(request, 'edit_character.html', context)


def create_series(request):
    """processing how our create series page renders"""
    if request.method == "POST":
        series_form = CreateSeriesForm(request.POST, request.FILES)
        if series_form.is_valid():
            series_form.save()
        return redirect(reverse('series_list'))
    series_form = CreateSeriesForm()
    context = {
        'series_form': series_form
    }
    return render(request, 'create_series.html', context)


def edit_series(request, series_id):
    """processing how we want to edit our series"""
    series = get_object_or_404(Series, id=series_id)
    if request.method == "POST":
        series_form = CreateSeriesForm(request.POST, request.FILES, instance=series)
        if series_form.is_valid():
            form.save()
            return redirect(reverse('series_list'))
    series_form = CreateSeriesForm(instance=series)
    context = {
        'series_form': series_form
    }
    return render(request, 'edit_series.html', context)


def delete_series(request, id):
    """processing how we delete a record from the series list"""
    context = {}
    series = get_object_or_404(Series, id=id)

    if request.method == "POST":
        series.delete()
        return redirect(reverse('series_list'))
    return render(request, 'delete_series.html', context)


class SuggestionList(generic.ListView):
    """this is the display of our Character model"""
    model = Suggestion
    queryset = Suggestion.objects.order_by('series_sug', 'char_sug')
    template_name = 'suggestions.html'
    paginate_by = 12


def create_sug(request):
    """processing how my suggestion form will render"""
    if request.method == "POST":
        sug_form = CreateSuggestionForm(request.POST)
        if sug_form.is_valid():
            sug_form.save()
        return redirect(reverse('suggestions'))
    sug_form = CreateSuggestionForm()
    context = {
        'sug_form': sug_form
    }
    return render(request, 'create_suggestion.html', context)



class CharacterList(generic.ListView):
    """this is the display of our Character model"""
    model = Character
    queryset = Character.objects.filter(status=1).order_by('series_name', 'name')
    template_name = 'index.html'
    paginate_by = 12


class SeriesList(generic.ListView):
    """This is to display the list of series I have added to my db"""
    model = Series
    queryset = Series.objects.order_by('series_name')
    template_name = 'series_list.html'
    paginate_by = 15


class Suggestionlist(generic.ListView):
    """"""


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
            },
        )
