# Generated by Django 3.2 on 2022-02-16 20:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collection', '0023_remove_series_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='char_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='votes',
            field=models.ManyToManyField(blank=True, related_name='character_rate', to=settings.AUTH_USER_MODEL),
        ),
    ]