# Generated by Django 3.2 on 2022-02-05 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0007_auto_20220205_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='special',
            field=models.CharField(default='None', max_length=200),
        ),
    ]
