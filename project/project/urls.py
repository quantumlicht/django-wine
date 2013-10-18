from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from .views import landing
from corewine.views import CepageCreateReadView
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', landing, name='landing'),
    url(r'^api/$',CepageCreateReadView.as_view(), name='cepage_rest_api'),
    url(r'^wine/', include('corewine.urls', namespace="corewine")),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
