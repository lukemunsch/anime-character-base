# Generated by Django 3.2 on 2022-02-03 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_auto_20220203_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='approved',
            field=models.BooleanField(default=0),
        ),
    ]
