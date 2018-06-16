# Gallery 657 #

A small picture gallery app with VueJs frontend and
Django backend.

## Installation ###
  
### Pip requirements ###

* Run: pip install -r require.txt

### Django settings ###

* Add 'gallery657' and 'rest_framework' to the INSTALLED_APPS setting.
* and add the restframework settings

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

* Run: python manage.py migrate
  
### Django url ###

  To the django projects' url.py add

  ``` python
  from django.conf.urls import include
  ```

  and

  ``` python
  url(r'^gallery/', include('gallery657.urls', namespace="gallery657" ),
```

### Django template ###

Unless you'r using a base.html for your site,
remove the first line in the templates/base_gallery657.html file.

``` html
{% extends "base.html" %}
```

## Live example ##

  www.oscfr.se/gallery

## App as component ##

If you whant to use the app as a component at a bigger site you create the div

``` html
<div id="gallery" >
  <router-view></router-view>
</div>
```

 where you whant the gallery to apear.

and preferbly put

``` html
<script src="{% static 'js/gallery657/dist/build.js' %}"></script>
```

at the bottom of your index.html



## For development ##

* Run: pip install pylint

* To the Django settings.py add

``` python
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

* To the Django project url.py add

``` python
from django.conf.urls.static import static
```

* and after the url patterns add, inclding the plus sign in the begining

``` python
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

* VueJS app building
  
  * Run: sudo apt-get install npm
  
  * In the vue_app directory run: npm run build
