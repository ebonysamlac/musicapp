from rest_framework import serializers

from .models import Artist, Songs, Lyrc

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ('id','first_name', 'last_name','age')

class SongsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Songs
        fields = ('title', 'date_released', 'likes', 'myartists_id')

class LyrcSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lyrc
        fields = ('content', 'mysongs_id')