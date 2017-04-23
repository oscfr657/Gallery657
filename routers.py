from rest_framework import routers
from gallery657.views import MediaFileViewSet


gallery657_router = routers.DefaultRouter()
gallery657_router.register(r'mediafiles', MediaFileViewSet)
