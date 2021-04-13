from rest_framework import serializers
from .models import *
from rest_framework.response import Response
from rest_framework import status
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator, MaxValueValidator


class AlbumCreationSerializer(serializers.ModelSerializer):
    album_name = serializers.CharField(validators=[MinLengthValidator(4)])
    genre = serializers.CharField()
    price = serializers.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(1000)])
    description = serializers.CharField()
    date_of_release = serializers.DateField()
    sung_by = serializers.PrimaryKeyRelatedField(many=True,  read_only=False, queryset=Musicians.objects.all())


    class Meta:
        model=MusicAlbums
        fields=('id','album_name','date_of_release','genre', 'price', 'description', 'sung_by')


class AlbumUpdateSerializer(serializers.ModelSerializer):
    album_id=serializers.IntegerField()
    album_name = serializers.CharField(validators=[MinLengthValidator(4)])
    genre = serializers.CharField()
    price = serializers.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(1000)])
    description = serializers.CharField()
    date_of_release = serializers.DateField()
    sung_by = serializers.PrimaryKeyRelatedField(many=True,  read_only=False, queryset=Musicians.objects.all())


    class Meta:
        model=MusicAlbums
        fields=('album_id','album_name','date_of_release','genre', 'price', 'description', 'sung_by') 




class MusicianCreationSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    musician_type = serializers.CharField()

    class Meta:
        model=Musicians
        fields='__all__'



class MusicianUpdationSerializer(serializers.ModelSerializer):
    musician_id = serializers.IntegerField()
    name = serializers.CharField()
    musician_type = serializers.CharField()

    class Meta:
        model=Musicians
        fields='__all__'


class AlbumDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = MusicAlbums
        fields = '__all__'


class AlbumRetrieveSerializer(serializers.ModelSerializer):
    # musician_id = serializers.IntegerField(required=True)

    class Meta:
        model=MusicAlbums
        fields='__all__'



class MusicianRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicAlbums
        fields = ( 'id', 'sung_by')


