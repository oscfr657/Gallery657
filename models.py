# -*- coding: utf-8 -*-
import magic
from time import time
from django.db import models
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
import StringIO
from PIL import Image
import os
# from django.utils import timezone


def unique_file_name(instance, filename):
    # Prepends unique epoch timestamp on image filename
    directory = 'gallery657'
    epoch_time = int(time())
    path = u"{}/{}-{}".format(directory, epoch_time, filename)
    return path

# TODO: Implement this.
video_types = ['video/mp4',
               'video/webm',
               'video/ogg']

image_types = ['image/png',
               'image/jpeg',
               'image/jpg',
               'image/gif',
               'image/svg']


def validate_file_type(media_file):
    try:
        file_type = magic.from_buffer(
            media_file.file.read(),
            mime=True)
        if not (file_type in image_types):
            raise ValidationError(
                u'File type not supported!')
    except (IOError, ValueError, AttributeError):
        raise ValidationError(u'File type not supported!')


class Collection(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        ordering = ['pk']

    def __unicode__(self):
        return u'%s' % self.title


class Art(models.Model):
    collection = models.ForeignKey(Collection,
                                   related_name="art",
                                   blank=True,
                                   null=True)
    media_file = models.FileField(upload_to=unique_file_name,
                                  validators=[validate_file_type])
    file_type = models.CharField(max_length=25,
                                 blank=True,
                                 null=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['pk']

    def __unicode__(self):
        if self.title:
            return u'%s' % self.title
        return ''

    def save(self):
        # First doing a normal save
        super(Art, self).save()
        # Then we try to optimize
        try:
            file_type = magic.from_buffer(
                self.media_file.file.read(),
                mime=True)
            image_file = self.media_file
            image = Image.open(image_file)
            ftype = image.format
            if image.mode not in ('L', 'RGBA'):
                image = image.convert('RGBA')
            picture_name, picture_extension = os.path.splitext(
                self.media_file.name)
            picture_extension = picture_extension.lower()
            picture_filename = picture_name + '_picture' + picture_extension
            image_copy = image.copy()
            image_copy.thumbnail((600, 600))
            image_file = StringIO.StringIO()
            image_copy.save(image_file, ftype, quality=90)
            image_file.seek(0)
            suf = SimpleUploadedFile(picture_filename,
                                     image_file.read(),
                                     content_type=file_type)
            self.media_file.save(suf.name, suf, save=False)
            super(Art, self).save()
        except (IOError, ValueError, AttributeError):
            pass  # We should probably log this.
