from django.apps import AppConfig
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from gallery657.views import gallery657


urlpatterns = patterns('',
    url(r'^$', gallery657, name='gallery'),
)
