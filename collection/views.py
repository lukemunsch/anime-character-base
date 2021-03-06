"""Set up the view for our models"""
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.views import generic, View
from .models import Character, Series, Suggestion, Comment
from .forms import CreateCharForm, AddSerForm, CreateSugForm, ComForm


def create_char(request):
    """processing our create character to render a view"""
    if request.method == "POST":
        char_form = CreateCharForm(request.POST, request.FILES)
        if char_form.is_valid():
            char_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Character Successfully Created'
            )
        return redirect(reverse('home'))
    char_form = CreateCharForm()
    context = {
        'char_form': char_form
    }
    return render(request, 'create_character.html', context)


def edit_char(request, slug):
    """process how to update a character"""
    char = get_object_or_404(Character, slug=slug)
    if request.method == "POST":
        char_form = CreateCharForm(
            request.POST,
            request.FILES,
            instance=char
        )
        if char_form.is_valid():
            char_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Character Successfully Updated'
            )
            return redirect(reverse('home'))
    char_form = CreateCharForm(instance=char)
    context = {
        'char_form': char_form
    }
    return render(request, 'edit_character.html', context)


def delete_char(request, slug):
    """process how we delete a character"""
    context = {}
    character = get_object_or_404(Character, slug=slug)

    if request.method == "POST":
        character.delete()
        messages.add_message(
            request,
            messages.ERROR,
            'Character Successfully Deleted'
        )
        return redirect(reverse('home'))
    return render(request, 'delete_character.html', context)


def create_series(request):
    """processing how our create series page renders"""
    if request.method == "POST":
        series_form = AddSerForm(request.POST, request.FILES)
        if series_form.is_valid():
            series_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Series Successfully Created'
                )
        return redirect(reverse('series_list'))
    series_form = AddSerForm()
    context = {
        'series_form': series_form
    }
    return render(request, 'create_series.html', context)


def edit_series(request, series_id):
    """processing how we want to edit our series"""
    series = get_object_or_404(Series, id=series_id)
    if request.method == "POST":
        series_form = AddSerForm(
            request.POST,
            request.FILES,
            instance=series
        )
        if series_form.is_valid():
            series_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Series Successfully Edited'
            )
            return redirect(reverse('series_list'))
    series_form = AddSerForm(instance=series)
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
        messages.add_message(
            request,
            messages.ERROR,
            'Series Successfully Deleted'
        )
        return redirect(reverse('series_list'))
    return render(request, 'delete_series.html', context)


class SuggestionList(generic.ListView):
    """this is the display of our Suggestion model"""
    model = Suggestion
    queryset = Suggestion.objects.order_by('series_sug', 'char_sug')
    template_name = 'suggestions.html'
    paginate_by = 12


def create_sug(request):
    """processing how my suggestion creation form will render"""
    if request.method == "POST":
        sug_form = CreateSugForm(request.POST)
        if sug_form.is_valid():
            sug_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Thank you for leaving me a suggestion!'
            )
        return redirect(reverse('suggestions'))
    sug_form = CreateSugForm()
    context = {
        'sug_form': sug_form
    }
    return render(request, 'create_suggestion.html', context)


def delete_sug(request, sug_id):
    """set up the deletion of suggestions from our list"""
    suggest = get_object_or_404(Suggestion, id=sug_id)
    suggest.delete()
    messages.add_message(
        request,
        messages.ERROR,
        'Suggestion Successfully Deleted'
    )
    return redirect('suggestions')


class CharacterList(generic.ListView):
    """this is the display of our Character model"""
    model = Character
    queryset = Character.objects.filter(status=1).order_by(
        'series_name',
        'name'
    )
    template_name = 'index.html'
    paginate_by = 10


class SeriesList(generic.ListView):
    """This is to display the list of series I have added to my db"""
    model = Series
    queryset = Series.objects.order_by('series_name')
    template_name = 'series_list.html'
    paginate_by = 15


class CharDetail(View):
    """creating the view for our character's main pages"""
    def get(self, request, slug, *args, **kwargs):
        """retrieving from the database"""
        queryset = Character.objects.all()
        character = get_object_or_404(queryset, slug=slug)
        comments = character.comments.all().order_by(
            '-created_on'
        )

        return render(
            request,
            "character_detail.html",
            {
                "character": character,
                "comments": comments,
                "commented": False,
                'comment_form': ComForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """set up how the post of our comments works"""
        queryset = Character.objects.filter(status=1)
        character = get_object_or_404(queryset, slug=slug)
        comments = character.comments.all().order_by(
            '-created_on'
        )

        comment_form = ComForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.character = character
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Thanks for posting a comment!!!'
            )
        else:
            comment_form = ComForm()

        return render(request, 'character_detail.html', {
            'character': character,
            'comments': comments,
            "commented": True,
            'comment_form': comment_form,
        })


def delete_comm(request, comm_id):
    """set up the deletion of comments from our list"""
    comment = get_object_or_404(Comment, id=comm_id)
    comment.delete()
    char_id = request.GET.get('charid')
    character = get_object_or_404(Character, pk=int(char_id))
    messages.add_message(
        request,
        messages.ERROR,
        'Comment Successfully Deleted'
    )
    return redirect('character_detail', slug=character.slug)
