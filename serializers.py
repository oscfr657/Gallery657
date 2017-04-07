
from rest_framework import serializers

from gallery657.models import MediaFile


class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ('pk', 'media_file', 'title', 'file_type', 'pub_date')
