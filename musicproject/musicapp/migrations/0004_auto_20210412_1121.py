# Generated by Django 3.2 on 2021-04-12 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_alter_musicalbums_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musicians',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Musician Name')),
                ('musician_type', models.CharField(choices=[('Vocalist', 'Vocalist'), ('Instrumentalist', 'Instrumentalist')], max_length=20, verbose_name='Musician Type')),
            ],
        ),
        migrations.AddField(
            model_name='musicalbums',
            name='sung_by',
            field=models.ManyToManyField(to='musicapp.Musicians'),
        ),
    ]
