
try:
    from django.urls import include, re_path as url
except ImportError:
    from django.conf.urls import url, include

from gallery657.views import gallery_vue
from gallery657.routers import GALLERY657_ROUTER


urlpatterns = [
    url(r'^api/', include(GALLERY657_ROUTER.urls)),
    url(r'^[\d+]*$', gallery_vue, name='gallery'),
]
