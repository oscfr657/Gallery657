
from django.conf.urls import url, include

from gallery657.views import gallery657, gallery_vue
from gallery657.routers import gallery657_router


urlpatterns = [
    url(r'^$', gallery_vue, name='gallery_vue'),
    #url(r'^old/', gallery657, name='gallery'),
    url(r'^api/', include(gallery657_router.urls)),
]
