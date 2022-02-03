"""Set up our imports"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Series(models.Model):
    """set up the series category"""
    id = models.IntegerField(primary_key=True)
    series_name = models.CharField(max_length=100, unique=True, null=False)
    approved = models.BooleanField(default=0)

    class Meta:
        ordering = ['series_name']

    def __str__(self):
        return self.series_name


VIEW_CARD = ((0, 'Hidden'), (1, 'Displayed'))


class Character(models.Model):
    """creating the model for our blog style character base"""
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    char_image = CloudinaryField('image', default='placeholder')
    series_name = models.ForeignKey(Series, on_delete=models.CASCADE, related_name="series")
    first_published = models.DateField(auto_now_add=True)
    first_aired = models.DateField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    bio = models.TextField(default="Enter bio here", max_length=1000)
    good_reason = models.CharField(default='', max_length=100)
    bad_reason = models.CharField(default='', max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=VIEW_CARD, default=0)
    likes = models.ManyToManyField(User, related_name='character_likes', blank=True)

    class Meta:
        """set up how we would like the cards to be ordered"""
        ordering = ['series_name', 'name']

    def __str__(self):
        return self.name

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """setting up the comment model under the bios"""
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(default='name', max_length=20, null=False)
    email = models.EmailField(default='e@mail.com', max_length=100)
    body = models.TextField(default='', max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """set the order for comments"""
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.name} | {self.email} says:'
