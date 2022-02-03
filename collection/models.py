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
    series = models.CharField(default='unknown', max_length=100)
    first_published = models.DateTimeField(auto_now_add=True)
    first_aired = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    bio = models.TextField(default="Enter bio here", max_length=300)
    good_reason = models.CharField(default='', max_length=100)
    bad_reason = models.CharField(default='', max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='character_likes', blank=True)

    class Meta:
        """set up how we would like the cards to be ordered"""
        ordering = ['name', 'series']

    def __str__(self):
        return self.name

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """setting up the comment model under the bios"""
    charcater = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='comment')
