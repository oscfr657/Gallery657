
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from gallery657.models import MediaFile


def gallery657(request):

    gallery = MediaFile.objects.all()
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


