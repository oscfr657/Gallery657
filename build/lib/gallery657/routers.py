from rest_framework import routers
from gallery657.views import ArtViewSet, CollectionViewSet


GALLERY657_ROUTER = routers.DefaultRouter()
GALLERY657_ROUTER.register(r'art', ArtViewSet)
GALLERY657_ROUTER.register(r'collection', CollectionViewSet)
