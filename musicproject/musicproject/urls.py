"""musicproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from musicapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/api_music_album_creation/', MusicAlbumCreation.as_view(), name='MusicAlbumCreation'),
    path('api/api_music_album_update/', MusicAlbumUpdate.as_view(), name='MusicAlbumUpdate'),
    path('api/api_musician_create/', MusiciainCreation.as_view(), name='MusiciainCreation'),
    path('api/api_musician_update/', MusiciainUpdation.as_view(), name='MusiciainUpdation'),

    path('api/api_album_data/', ALbumDataAPI.as_view(), name='ALbumDataAPI'),
    path('api/api_album_retrieve/', AlbumRetrieveAPI.as_view(), name='AlbumRetrieveAPI'),
    path('api/api_musician_retrieve/', MusicianRetrieveAPI.as_view(), name='MusicianRetrieveAPI'),

]
