
from django.utils import timezone

from django.db.models import Q

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.exceptions import NotFound

from gallery657.models import Art, Collection
from gallery657.serializers import ArtSerializer, CollectionSerializer


def gallery657(request):
    gallery = Art.objects.all().order_by('-pub_date')
    paginator = Paginator(gallery, 1)
    page = request.GET.get('page')
    try:
        arts = paginator.page(page)
    except PageNotAnInteger:
        arts = paginator.page(1)
    except EmptyPage:
        arts = paginator.page(paginator.num_pages)
    dictionary = {'gallery': arts}
    return render(request, 'gallery657.html', dictionary)


def gallery_vue(request):
    return render(request, 'gallery_vue.html')


class ArtViewSet(ReadOnlyModelViewSet):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer
    pagination_class = None

    def get_queryset(self):
        queryset = Art.objects.filter(
            Q(pub_date__lte=timezone.now()) | Q(pub_date=None))
        collection = self.request.query_params.get('collection', None)
        if collection:
            try:
                queryset = queryset.filter(collection=collection)
            except ValueError:
                raise NotFound
        return queryset


class CollectionViewSet(ReadOnlyModelViewSet):
    queryset = Collection.objects.filter(
        Q(pub_date__lte=timezone.now()) | Q(pub_date=None))
    serializer_class = CollectionSerializer
    pagination_class = None
