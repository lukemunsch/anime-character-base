"""Set up the view for our models"""
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Character, Series, Comment


class CharacterList(generic.ListView):
    """this is the display of our Character model"""
    model = Character
    queryset = Character.objects.filter(status=1).order_by('-series_name')
    template_name = 'index.html'
    paginate_by = 8


class CharacterDetail(View):
    """this will display the view for the opened character profile"""
    def get(self, request, slug, args, kwargs):
        """set up how the page will be displayed in character_detail.html"""
        queryset = Character.object.filter(status=1)
        character = get_object_or_404(queryset, slug=slug)
        comments = character.comments.filter(approved=True).order_by('created_on')
        liked = False
        if character.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "character_details.html",
            {
                "character": character,
                "comments": comments,
                "liked": liked
            }
        )
