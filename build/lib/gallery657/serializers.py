
from rest_framework import serializers

from gallery657.models import Art, Collection


class ArtSerializer(serializers.ModelSerializer):

    class Meta:
        model = Art
        fields = ('pk', 'title', 'collection', 'thumb_nail', 'media_file', 'file_type', 'pub_date')


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ('pk', 'title', 'slug')
