"""Set up our imports"""
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField


class Series(models.Model):
    """set up the series category"""
    series_name = models.CharField(max_length=100, unique=True, null=False)
    series_logo = CloudinaryField('image', default='placeholder')
    approved = models.BooleanField(default=1)

    class Meta:
        """set up how they will appear on the screen"""
        ordering = ['series_name']

    def __str__(self):
        return self.series_name


VIEW_CARD = ((0, 'Hidden'), (1, 'Displayed'))


class Character(models.Model):
    """creating the model for our blog style character base"""
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    char_image = CloudinaryField('image', default='placeholder')
    series_name = models.ForeignKey(
        Series,
        on_delete=models.CASCADE,
        related_name="series"
    )
    first_published = models.DateField(null=True, blank=True)
    first_aired = models.DateField(null=True, blank=True)
    age = models.PositiveIntegerField(default=0)
    bio = models.TextField(default='', max_length=4000)
    special = models.CharField(max_length=200)
    good_reason = models.CharField(default='', max_length=100)
    bad_reason = models.CharField(default='', max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=VIEW_CARD, default=1)

    class Meta:
        """set up how we would like the cards to be ordered"""
        ordering = ['series_name', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.series_name}-{self.name}')
        return super().save(*args, **kwargs)


class Comment(models.Model):
    """setting up the comment model under the bios"""
    character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    name = models.CharField(null=False, max_length=80)
    body = models.TextField(default='', max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        """set the order for comments"""
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} | {self.name}'


SUG_TYPE = ((0, "Character"), (1, "Series"))


class Suggestion(models.Model):
    """sets up the model for user suggestions for me to add to my site"""
    sug_type = models.IntegerField(choices=SUG_TYPE, default=1)
    char_sug = models.CharField(max_length=100, null=True)
    series_sug = models.CharField(max_length=100, null=False)
    reason = models.CharField(max_length=100, null=False)
    created_when = models.DateTimeField(auto_now_add=True)

    class Meta:
        """set up our order for suggestions"""
        ordering = ['created_when']

    def __str__(self):
        return f'{self.sug_type} | {self.created_when}'
