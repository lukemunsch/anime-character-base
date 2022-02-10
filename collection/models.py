"""Set up our imports"""
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField


class Series(models.Model):
    """set up the series category"""
    id = models.IntegerField(primary_key=True)
    series_name = models.CharField(max_length=100, unique=True, null=False)
    series_logo = CloudinaryField('image', default='placeholder')
    approved = models.BooleanField(default=0)

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
    series_name = models.ForeignKey(Series, on_delete=models.CASCADE, related_name="series")
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


class Suggestion(models.Model):
    """sets up the model for user suggestions for me to add to my site"""
    char_sug = models.CharField(max_length=100, null=False)
    series_sug = models.CharField(max_length=100, null=False)
    reason = models.CharField(max_length=100, null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="name")
    created_when = models.DateTimeField(auto_now_add=True)

    class Meta:
        """set up our order for suggestions"""
        ordering = ['created_when']

    def __str__(self):
        return self.char_sug
