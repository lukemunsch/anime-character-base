# Generated by Django 3.2 on 2022-02-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0014_alter_character_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='first_aired',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='first_published',
            field=models.DateField(blank=True, null=True),
        ),
    ]