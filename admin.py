from django.contrib import admin

from gallery657.models import Art, Collection

# Customize this, plz.
admin.site.register(Collection)

admin.site.register(Art)
