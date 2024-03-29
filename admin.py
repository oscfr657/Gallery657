# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.sites.shortcuts import get_current_site

from gallery657.models import Art, Collection


class ArtAdmin(admin.ModelAdmin):
    fields = ('collection', 'title', 'pub_date', 'media_file',
              'thumb_nail', 'file_type')
    readonly_fields = ('file_type', 'thumb_nail')
    list_display = ('title', 'pub_date', 'file_type', 'collection')
    date_hierarchy = 'pub_date'


class ArtInline(admin.TabularInline):
    model = Art
    extra = 1
    fields = ('title', 'pub_date', 'media_file', 'thumb_nail', 'file_type')
    readonly_fields = ('file_type', 'thumb_nail', )


class CollectionAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    inlines = [ArtInline,]
    list_display = ('title', 'pub_date')
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        return ['sites']

    def get_queryset(self, request):
        qs = super(CollectionAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(sites=get_current_site(request))

    def save_related(self, request, form, formsets, change):
        super(CollectionAdmin, self).save_related(request, form, formsets, change)
        if not request.user.is_superuser:
            form.instance.sites.add(get_current_site(request))


admin.site.register(Art, ArtAdmin)
admin.site.register(Collection, CollectionAdmin)
