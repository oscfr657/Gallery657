# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from time import time
from django.core.exceptions import ValidationError


def unique_file_name(instance, filename):
    # Prepends unique epoch timestamp on image filename
    directory = 'gallery657'
    epoch_time = int(time())
    path = u"{}/{}-{}".format(directory, epoch_time, filename)
    return path


def validate_file_type(media_file):
    try:
        file_type = media_file.file.content_type
        valid_types = ['video/mp4',
                       'video/webm',
                       'video/ogg',
                       'image/png',
                       'image/jpeg']
        if not file_type in valid_types:
            raise ValidationError(u'File type not supported!')
    except ValueError:
        pass
    

class MediaFile(models.Model):
    media_file = models.FileField(upload_to=unique_file_name,
                                  validators=[validate_file_type])
    file_type = models.CharField(max_length=50)
    pub_date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        if self.title:
            return u'%s' % self.title
        return ''

