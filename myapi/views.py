from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ArtistSerializer, SongsSerializer, LyrcSerializer
from .models import Artist, Songs, Lyrc
# Create your views here.


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('first_name')
    serializer_class = ArtistSerializer

class SongsViewSet(viewsets.ModelViewSet):
    queryset = Songs.objects.all().order_by('title')
    serializer_class = SongsSerializer


class LyrcViewSet(viewsets.ModelViewSet):
    queryset = Lyrc.objects.all().order_by('mysongs_id')
    serializer_class = LyrcSerializer

class ArtistDetailApiView(APIView):


    def get_object(self, artist_id):
        '''
        Helper method to get the object with given artist_id
        '''
        try:
            return Artist.objects.get(id=artist_id)
        except Artist.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, artist_id, *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        artist_instance = self.get_object(artist_id)
        if not artist_instance:
            return Response(
                {"res": "Object with Artist id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ArtistSerializer(artist_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, artist_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        artist_instance = self.get_object(artist_id)
        if not artist_instance:
            return Response(
                {"res": "Object with Artist id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'first_name': request.data.get('first_name'), 
            'last_name': request.data.get('last_name'), 
            'age': request.data.get('age'),
        }
        serializer = ArtistSerializer(instance = artist_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, artist_id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        artist_instance = self.get_object(artist_id)
        if not artist_instance:
            return Response(
                {"res": "Object with Artist id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        artist_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )