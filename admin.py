# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from gallery657.models import Art, Collection


class ArtAdmin(admin.ModelAdmin):
    fields = ('collection', 'title', 'pub_date', 'media_file',
              'thumb_nail', 'file_type')
    readonly_fields = ('file_type', 'thumb_nail')
    date_hierarchy = 'pub_date'


class ArtInline(admin.TabularInline):
    model = Art
    extra = 1
    fields = ('title', 'pub_date', 'media_file', 'thumb_nail', 'file_type')
    readonly_fields = ('file_type', 'thumb_nail', )


class CollectionAdmin(admin.ModelAdmin):
    date_hierarchy = 'art__pub_date'
    inlines = [ArtInline,]


admin.site.register(Art, ArtAdmin)
admin.site.register(Collection, CollectionAdmin)
