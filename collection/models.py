"""Set up our imports"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, 'Draft'), (1, 'Published'))


class Character(models.Model):
    """creating the model for our blog style character base"""
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    char_image = CloudinaryField('image', default='placeholder')
    series = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    age = models.PositiveIntegerField(default=0)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='character_likes', blank=True)

    class Meta:
        """set up how we would like the cards to be ordered"""
        ordering = ['name', 'series']

    def __str__(self):
        return self.name

    def number_of_likes(self):
        return self.likes.count()
