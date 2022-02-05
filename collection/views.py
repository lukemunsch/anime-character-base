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
    """creating he view for our character's main pages"""
    def get(self, request, slug, *args, **kwargs):
        """retrieving from the database"""
        queryset = Character.objects.filter(status=1)
        character = get_object_or_404(queryset, slug=slug)
        comments = character.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "character_detail.html",
            {
                "character": character,
                "commented": False,
                "liked": liked,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """setting up the post for the comments"""
        queryset = Character.objects.filter(status=1)
        character = get_object_or_404(queryset, slug=slug)
        comments = character.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "character_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class CharacterLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
