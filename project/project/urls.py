from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import landing

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', landing, name='landing'),
    url(r'^api/', include('core.api', namespace="api" )),
    url(r'^wine/', include('corewine.urls', namespace="corewine")),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
