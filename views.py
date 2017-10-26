
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from rest_framework.viewsets import ReadOnlyModelViewSet

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

    def get_queryset(self):
        queryset = Art.objects.all()
        collection = self.request.query_params.get('collection', None)
        if collection is not None:
            queryset = queryset.filter(collection=collection)
        return queryset


class CollectionViewSet(ReadOnlyModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
