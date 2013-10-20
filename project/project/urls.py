from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import landing
from corewine.views import CepageReadView, TagReadView, TeintReadView
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', landing, name='landing'),
    url(r'^api/cepage$',CepageReadView.as_view(), name='cepage_rest_api'),
    url(r'^api/tag$',TagReadView.as_view(), name='tag_rest_api'),
    url(r'^api/teint$',TeintReadView.as_view(), name='teint_rest_api'),
    url(r'^wine/', include('corewine.urls', namespace="corewine")),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
