from rest_framework import routers
from gallery657.views import MediaFileViewSet, CollectionViewSet


gallery657_router = routers.DefaultRouter()
gallery657_router.register(r'media_file', MediaFileViewSet)
gallery657_router.register(r'collection', CollectionViewSet)
