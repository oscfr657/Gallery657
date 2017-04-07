# -*- coding: utf-8 -*-

import magic
from time import time

from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


def unique_file_name(instance, filename):
    # Prepends unique epoch timestamp on image filename
    directory = 'gallery657'
    epoch_time = int(time())
    path = u"{}/{}-{}".format(directory, epoch_time, filename)
    return path

video_types = ['video/mp4',
               'video/webm',
               'video/ogg']

image_types = ['image/png',
               'image/jpeg',
               'image/jpg']


def validate_file_type(media_file):
    try:
        file_type = magic.from_buffer(
            media_file.file.read(),
            mime=True)
        if not (file_type in video_types or file_type in image_types):
            raise ValidationError(
                u'File type not supported!')
    except (IOError, ValueError, AttributeError):
        raise ValidationError(u'File type not supported!')


class MediaFile(models.Model):
    media_file = models.FileField(upload_to=unique_file_name,
                                  validators=[validate_file_type])
    file_type = models.CharField(max_length=50)
    pub_date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['pk']

    def __unicode__(self):
        if self.title:
            return u'%s' % self.title
        return ''
