# -*- coding: utf-8 -*-
import os
from io import BytesIO
from time import time

import magic
from PIL import Image

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
try:
    from django.core.urlresolvers import reverse
except ImportError:
    from django.urls import reverse

from django.contrib.sites.models import Site

from django.db import models

# TODO: Why not this ?
# from django.utils import timezone


DIRECTORY = 'gallery657'


def unique_file_name(instance, filename):
    # Prepends unique epoch timestamp on image filename
    epoch_time = int(time())
    path = u'{}/{}-{}'.format(DIRECTORY, epoch_time, filename)
    return path


# TODO: Implement this.
VIDEO_TYPES = ['video/mp4',
               'video/webm',
               'video/ogg']

IMAGE_TYPES = ['image/png',
               'image/jpeg',
               'image/jpg',
               'image/gif',
               'image/svg']


def validate_file_type(media_file):
    try:
        file_type = magic.from_buffer(
            media_file.file.read(),
            mime=True)
        if file_type not in IMAGE_TYPES:
            raise ValidationError(
                u'File type not supported!')
    except (IOError, ValueError, AttributeError):
        raise ValidationError(u'File type not supported!')


class Collection(models.Model):
    sites = models.ManyToManyField(Site)
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(blank=True, null=True)

    slug = models.SlugField(unique=True, max_length=100, blank=True, null=True)

    objects = models.Manager()

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = 'Collections'

    def __unicode__(self):
        return u'%s' % self.title

    def __str__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return '/gallery/#/' + self.slug


class Art(models.Model):
    collection = models.ForeignKey(Collection,
                                   on_delete=models.SET_NULL,
                                   related_name="art",
                                   blank=True,
                                   null=True)
    media_file = models.FileField(upload_to=unique_file_name,
                                  validators=[validate_file_type])
    file_type = models.CharField(max_length=25,
                                 blank=True,
                                 null=True)
    thumb_nail = models.FileField(blank=True, null=True,
                                  upload_to=DIRECTORY,
                                  validators=[validate_file_type])
    pub_date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)

    objects = models.Manager()

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = 'Works of art'

    def __unicode__(self):
        if self.title:
            return u'%s' % self.title
        return u'%s' % self.pk

    def __str__(self):
        if self.title:
            return u'%s' % self.title
        return u'%s' % self.pk

    def save(self):
        # First doing a normal save
        super(Art, self).save()
        # Then we try to optimize
        try:
            media_file = self.media_file
            file_type = magic.from_buffer(
                media_file.file.read(),
                mime=True)
            self.file_type = file_type
            if file_type in IMAGE_TYPES:
                image = Image.open(media_file)
                ftype = image.format
                picture_name, picture_extension = os.path.splitext(
                    media_file.name)
                picture_extension = picture_extension.lower()
                thumb_filename = picture_name + '_thumb' + picture_extension
                image.thumbnail((600, 600), Image.ANTIALIAS)
                try:  # Handle orientation
                    image_exif = image._getexif()
                    image_orientation = image_exif[274]
                    if image_orientation in (2,'2'):
                        image = image.transpose(Image.FLIP_LEFT_RIGHT)
                    elif image_orientation in (3,'3'):
                        image = image.transpose(Image.ROTATE_180)
                    elif image_orientation in (4,'4'):
                        image = image.transpose(Image.FLIP_TOP_BOTTOM)
                    elif image_orientation in (5,'5'):
                        image = image.transpose(Image.ROTATE_90).transpose(Image.FLIP_TOP_BOTTOM)
                    elif image_orientation in (6,'6'):
                        image = image.transpose(Image.ROTATE_270)
                    elif image_orientation in (7,'7'):
                        image = image.transpose(Image.ROTATE_270).transpose(Image.FLIP_TOP_BOTTOM)
                    elif image_orientation in (8,'8'):
                        image = image.transpose(Image.ROTATE_90)
                except (KeyError, AttributeError, TypeError, IndexError):
                    pass  # We should probably handle and or log this.
                thumb_file = BytesIO()
                image.save(thumb_file, ftype, quality=90)
                thumb_file.seek(0)
                suf = SimpleUploadedFile(thumb_filename,
                                        thumb_file.read(),
                                        content_type=file_type)
                self.thumb_nail.save(suf.name, suf, save=False)
            super(Art, self).save()
        except (IOError, ValueError, AttributeError):
            pass  # We should probably handle and or log this.
