# Generated by Django 3.2 on 2022-02-10 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0016_alter_series_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='approved',
            field=models.BooleanField(default=1),
        ),
    ]