
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from rest_framework.viewsets import ReadOnlyModelViewSet

from gallery657.models import MediaFile, Collection
from gallery657.serializers import MediaFileSerializer, CollectionSerializer


def gallery657(request):
    gallery = MediaFile.objects.all().order_by('-pub_date')
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


class MediaFileViewSet(ReadOnlyModelViewSet):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = MediaFile.objects.all()
        collection = self.request.query_params.get('collection', None)
        if collection is not None:
            queryset = queryset.filter(collection=collection)
        return queryset


class CollectionViewSet(ReadOnlyModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
