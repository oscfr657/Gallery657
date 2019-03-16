
# Gallery 657 #

A small picture gallery app with VueJs frontend and
Django backend.

## Installation ###
  
### Pip requirements ###

> pip install -r requirements.txt

### Django settings ###

Add 'gallery657' and 'rest_framework' to the INSTALLED_APPS settings

Add this restframework settings

``` python
  REST_FRAMEWORK {
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    )
  }
```

### Database configuration ###

> python manage.py migrate
  
### Django url ###

To the django projects' url.py add

``` python
from django.conf.urls import include
from gallery657.sitemap import GallerySitemap
```

``` python
SITEMAPS = {
    'gallery': GallerySitemap,
}
```

``` python
    url(r'^gallery/', include('gallery657.urls', namespace="gallery657" ),
    url(r'^sitemap\.xml$', sitemaps_views.index, {'sitemaps': SITEMAPS}),
    url(r'^sitemap-(?P<section>.+)\.xml$', sitemaps_views.sitemap, {'sitemaps': SITEMAPS},
        name='django.contrib.sitemaps.views.sitemap'),
```

### Django template ###

Unless you'r using a base.html for your site,
remove the first line in the templates/base_gallery657.html file.

``` html
{% extends "base.html" %}
```

## App as component ##

If you whant to use the app as a component at a bigger site you create the div

``` html
<div id="gallery657" >
  <router-view></router-view>
</div>
```

 where you whant the gallery to apear.

and preferbly put

``` html
<script src="{% static 'js/gallery657/dist/build.js' %}"></script>
```

at the bottom of your index.html

## Live example ##

  www.oscfr.se/gallery

## For development ##

> pip install pylint

To the Django settings.py add

``` python
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

To the Django project url.py add

``` python
from django.conf.urls.static import static
```

After the url patterns add, inclding the plus sign in the begining

``` python
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### VueJS app building ###

 > sudo apt-get install npm
  
 In the vue_app directory run:

> npm install

and

> npm run build
