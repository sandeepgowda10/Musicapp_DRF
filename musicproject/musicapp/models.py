from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

MUSICIAN_TYPE = (
    ('Vocalist', 'Vocalist'),
    ('Instrumentalist', 'Instrumentalist'),
)



class Musicians(models.Model):
    name = models.CharField(max_length=50, verbose_name="Musician Name")
    musician_type = models.CharField(max_length=20, choices=MUSICIAN_TYPE, verbose_name="Musician Type")

    def __str__(self):
        return self.name




class MusicAlbums(models.Model):
    album_name = models.CharField(validators=[MinLengthValidator(4)], max_length=50)
    date_of_release = models.DateField(verbose_name="Date Of Release")
    genre = models.CharField(max_length=30, verbose_name="Type Of Music")
    price = models.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(1000)])
    description = models.TextField()
    sung_by = models.ManyToManyField(Musicians)

    def __str__(self):
        return self.album_name


 


