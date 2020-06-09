
# Gallery 657 #

A small picture gallery app with VueJs frontend and
Django backend.

## Setup ###
  
### Pip requirements ###

> pip install -r requirements.txt

### Django settings ###

Add to your settings file.

``` Python
SITE_ID = 1
```

add to the INSTALLED_APPS

``` Python
    'django.contrib.sites',

    'rest_framework',

    'gallery657',
```

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
```

``` python
    path('gallery657/', include('gallery657.urls', namespace='gallery657')),
```

### HTML ###

Where you want the app you put the div

``` html
<div id="gallery657" >
  <router-view></router-view>
</div>
```

where you whant the gallery to apear.

and preferbly put

``` html
<link rel="stylesheet" type="text/css" href="/static/css/gallery657/gallery_base.css" >
```

in the header and


``` html
<script src="static/js/gallery657/dist/build.js" async=""></script>
<script src="static/js/gallery657/dist/build.js.map" async=""></script>
```

at the bottom of your base.html

## Optional ##

### Sitemap ###

Add to the INSTALLED_APPS

``` Python
    'django.contrib.sitemaps',
```

To the django projects' url.py add

``` python
from django.contrib.sitemaps import views as sitemaps_views
from gallery657.sitemap import GallerySitemap
```

``` python
SITEMAPS = {
    'sitemaps': GallerySitemap
}
```

and add to the urlpatterns

``` python
    url(r'^sitemap\.xml$', sitemaps_views.index, {'sitemaps': SITEMAPS}),
```

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
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

#### For debuging ####

Add to settings

``` python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'logfile': {
            'level':'DEBUG',
            'class':'logging.FileHandler',
            'filename': BASE_DIR + "/debug.log",
        },
    },
    'loggers': {
        'gallery657': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
        },
    }
}
```
and where you need to debug add

``` python
import logging
logger = logging.getLogger('gallery657')

logger.debug('debug message')
```

### VueJS app building ###

 > sudo apt-get install npm
  
 In the vue_app directory run:

> npm install

and

> npm run build
