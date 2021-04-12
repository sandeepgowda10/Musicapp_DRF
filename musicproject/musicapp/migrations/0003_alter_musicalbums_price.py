# Generated by Django 3.2 on 2021-04-12 18:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_alter_musicalbums_album_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicalbums',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(1000)]),
        ),
    ]
