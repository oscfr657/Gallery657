# Gallery 657 #

A small picture gallery VueJs app with Django backend.

## Installation ###
  
### Pip requirements

  * Run: pip install -r require.txt

    #### for development

    * pip install pylint
    
### Django settings

  * Add 'gallery657' and 'rest_framework' to the INSTALLED_APPS setting.
  * and add the restframework settings
  ```
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

  * #### for development
    add
    ```
        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    ```

### Django url
  To the django projects' url.py add
  ```
  from django.conf.urls import include
  ```
  and
  ```
  url(r'^gallery/', include('gallery657.urls', namespace="gallery657" ),
```  
  

  * #### for development
    add
    ```
    from django.conf.urls.static import static
    ```
    and after the url patterns add
    ```
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

### Database configuration

  Run: python manage.py migrate
  
### VueJS app building
  
  Run: sudo apt-get install npm
  
  In the vue_app directory run: npm run build
  


#### Live example ####
  www.oscfr.se/gallery
  
