
from django.contrib.sitemaps import Sitemap
from django.utils import timezone

from gallery657.models import Collection


class GallerySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        collections = Collection.objects.filter(
            pub_date__isnull=False).filter(
                pub_date__lte=timezone.now()
                ).order_by('-pub_date')
        return collections

    def lastmod(self, obj):
        art = obj.art.filter(
            pub_date__isnull=False).filter(
                pub_date__lte=timezone.now()
                ).latest('pub_date')
        return obj.pub_date if obj.pub_date > art.pub_date else art.pub_date
