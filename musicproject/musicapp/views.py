from django.shortcuts import render
from .serializers import *
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import generics
from django.http import JsonResponse

# Create your views here.
#1st API
@permission_classes((permissions.AllowAny,))
class MusicAlbumCreation(APIView):
    serializer_class = AlbumCreationSerializer

    def post(self, request):
        serializing = self.serializer_class(data=request.data)
        serializing.is_valid(raise_exception=True)

        try:
            data = MusicAlbums()
            data.album_name = serializing.data['album_name']
            data.date_of_release = serializing.data['date_of_release']
            data.genre = serializing.data['genre']
            data.price = serializing.data['price']
            data.description = serializing.data['description']
            data.save()
            users =serializing.data['sung_by'] 
            data.sung_by.add(*users)
            data.save()

            return Response(
                {
                    "status": True,
                    "resultCode": status.HTTP_200_OK,
                    "message": 'Music Album is created successfully'
                },
                status=status.HTTP_200_OK

            )
        except:
            return Response(
                {

                    "message": "Some Issue",
                    "resultCode": status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST

            )


#1st API
@permission_classes((permissions.AllowAny,))
class MusicAlbumUpdate(APIView):
    serializer_class = AlbumUpdateSerializer

    def put(self, request):
        serializing = self.serializer_class(data=request.data)
        serializing.is_valid(raise_exception=True)

        try:
            try:
                data = MusicAlbums.objects.get(id=serializing.data['album_id'])
            except:
                return Response(
                {

                    "message": "Album Doesn't exist",
                    "resultCode": status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST

            )
            data.album_name = serializing.data['album_name']
            data.date_of_release = serializing.data['date_of_release']
            data.genre = serializing.data['genre']
            data.price = serializing.data['price']
            data.description = serializing.data['description']
            data.save()
            users =serializing.data['sung_by'] 
            data.sung_by.clear()
            data.sung_by.add(*users)
            data.save()

            return Response(
                {
                    "status": True,
                    "resultCode": status.HTTP_200_OK,
                    "message": 'Music Album is Updated successfully'
                },
                status=status.HTTP_200_OK

            )
        except:
            return Response(
                {

                    "message": "Some Issue",
                    "resultCode": status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST

            )



#2nd API
@permission_classes((permissions.AllowAny,))
class MusiciainCreation(APIView):
    serializer_class = MusicianCreationSerializer

    def post(self, request):
        serializing = self.serializer_class(data=request.data)
        serializing.is_valid(raise_exception=True)

        try:
        
            data = Musicians()
            data.name = serializing.data['name']
            data.musician_type = serializing.data['musician_type']
            data.save()

            return Response(
                {
                    "status": True,
                    "resultCode": status.HTTP_200_OK,
                    "message": 'Musician Created Successfully'
                },
                status=status.HTTP_200_OK

            )
        except:
            return Response(
                {

                    "message": "Some Issue",
                    "resultCode": status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST

            )



#2nd API
@permission_classes((permissions.AllowAny,))
class MusiciainUpdation(APIView):
    serializer_class = MusicianUpdationSerializer

    def put(self, request):
        serializing = self.serializer_class(data=request.data)
        serializing.is_valid(raise_exception=True)

        try:
            try:
                data = Musicians.objects.get(id=serializing.data['musician_id'])
            except:
                return Response(
                {

                    "message": "Musician Doesn't exist",
                    "resultCode": status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST

            )

            data.name = serializing.data['name']
            data.musician_type = serializing.data['musician_type']
            data.save()

            return Response(
                {
                    "status": True,
                    "resultCode": status.HTTP_200_OK,
                    "message": 'Musician Updated Successfully'
                },
                status=status.HTTP_200_OK

            )
        except:
            return Response(
                {

                    "message": "Some Issue",
                    "resultCode": status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST

            )

#3rd API
@permission_classes((permissions.AllowAny,))
class ALbumDataAPI(generics.ListAPIView):
    serializer_class = AlbumDataSerializer
    queryset = MusicAlbums.objects.all().order_by('-date_of_release')
    search_fields = ['batch_no']

    def get(self, request, *args, **kwargs):
        response = super(ALbumDataAPI, self).get(request, *args, **kwargs)
        return response


        
#4th API
@permission_classes((permissions.AllowAny,))
class AlbumRetrieveAPI(generics.ListAPIView):
    serializer_class = AlbumRetrieveSerializer

    def get_queryset(self):
        try:
            records = self.request.query_params['musician_id']
        except:
            pass
        try:
  
            queryset = MusicAlbums.objects.filter(sung_by__id=self.request.GET['musician_id']).order_by('price')
            
        except:
            pass
        return queryset


    def get(self, request, *args, **kwargs):
        response = super(AlbumRetrieveAPI, self).get(request, *args, **kwargs)
        return response



#5th API
@permission_classes((permissions.AllowAny,))
class MusicianRetrieveAPI(generics.ListAPIView):
    serializer_class = MusicianRetrieveSerializer

    def get_queryset(self):
        try:
            records = self.request.query_params['album_id']
        except:
            pass
        try:
  
            queryset = MusicAlbums.objects.filter(id=records)
            
        except:
            pass
        return queryset


    def get(self, request, *args, **kwargs):
        response = super(MusicianRetrieveAPI, self).get(request, *args, **kwargs)
        return response
