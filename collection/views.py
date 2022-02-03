"""Set up the view for our models"""
from django.shortcuts import render, request
from django.views import generic
from .models import Character, Series, Comment


def Index(request):
    return render(request, 'index.html')


class CharacterCards(generic.ListView):
    """this is the display of our Character model"""
    model = Character
    queryset = Character.objects.filter(status=1).order_by('-created_on')
    template_name = 'characters.html'
    paginate_by = 10
