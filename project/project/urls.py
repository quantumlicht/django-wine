from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from .views import landing
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', landing, name='landing'),
    url(r'^wine/', include('corewine.urls', namespace="corewine")),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
