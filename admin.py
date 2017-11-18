from django.contrib import admin

from gallery657.models import Art, Collection


class ArtAdmin(admin.ModelAdmin):
    fields = ('title', 'pub_date', 'media_file',
              'thumb_nail', 'file_type', 'collection')
    readonly_fields = ('file_type', 'thumb_nail', 'collection')
    date_hierarchy = 'pub_date'


class ArtInline(admin.TabularInline):
    model = Art
    fields = ('title', 'pub_date', 'thumb_nail', 'media_file', 'file_type')
    readonly_fields = ('file_type', 'pub_date', 'thumb_nail', 'media_file', )


class CollectionAdmin(admin.ModelAdmin):
    date_hierarchy = 'art__pub_date'
    inlines = [
            ArtInline,
        ]


admin.site.register(Art, ArtAdmin)
admin.site.register(Collection, CollectionAdmin)
