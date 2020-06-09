
from django.utils import timezone

from django.db.models import Q

from django.shortcuts import render

from django.contrib.sites.shortcuts import get_current_site

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.exceptions import NotFound

from gallery657.models import Art, Collection
from gallery657.serializers import ArtSerializer, CollectionSerializer


def gallery_vue(request):
    return render(request, 'gallery_base.html')


class ArtViewSet(ReadOnlyModelViewSet):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer

    def get_queryset(self):
        try:
            from wagtail.core.models import Site as WagtailSite
            wagtail_site = WagtailSite.find_for_request(self.request)
            from django.contrib.sites.models import Site
            current_site = Site.objects.get(domain=wagtail_site.hostname)
        except Exception as e:
            current_site = get_current_site(self.request)
        queryset = Art.objects.filter(
            Q(pub_date__lte=timezone.now()) | Q(pub_date=None)).filter(
                collection__sites=current_site).filter(
                    Q(collection__pub_date__lte=timezone.now()) | Q(
                        collection__pub_date__isnull=False)
                )
        collection = self.request.query_params.get('collection', None)
        if collection:
            try:
                queryset = queryset.filter(collection=collection)
            except ValueError:
                raise NotFound
        return queryset


class CollectionViewSet(ReadOnlyModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = None

    def get_queryset(self):
        try:
            from wagtail.core.models import Site as WagtailSite
            wagtail_site = WagtailSite.find_for_request(self.request)
            from django.contrib.sites.models import Site
            current_site = Site.objects.get(domain=wagtail_site.hostname)
        except Exception as e:
            current_site = get_current_site(self.request)
        queryset = Collection.objects.filter(
            Q(pub_date__lte=timezone.now()) | Q(pub_date__isnull=False)).filter(
                sites=current_site)
        return queryset
