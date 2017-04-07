from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
from gallery657.views import MediaFileViewSet


gallery657_router = routers.DefaultRouter()
gallery657_router.register(r'mediafiles', MediaFileViewSet)
