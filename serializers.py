
from rest_framework import serializers

from gallery657.models import MediaFile, Collection


class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ('pk', 'collection', 'media_file', 'title', 'file_type', 'pub_date')


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ('pk', 'title')
