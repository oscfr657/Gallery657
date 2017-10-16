from rest_framework import routers
from gallery657.views import ArtViewSet, CollectionViewSet


gallery657_router = routers.DefaultRouter()
gallery657_router.register(r'art', ArtViewSet)
gallery657_router.register(r'collection', CollectionViewSet)
