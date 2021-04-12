# Generated by Django 3.2 on 2021-04-12 18:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicAlbums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 4', regex='^.{4}$')])),
                ('date_of_release', models.DateField(verbose_name='Date Of Release')),
                ('genre', models.CharField(max_length=30, verbose_name='Type Of Music')),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]