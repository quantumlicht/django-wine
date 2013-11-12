from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import landing, set_language, set_lang

admin.autodiscover()

js_info_dict = {
    'packages': ('corewine',),
}


urlpatterns = patterns('',
    url(r'^$', landing, name='landing'),
    url(r'^api/', include('core.api', namespace="api" )),
    url(r'^wine/', include('corewine.urls', namespace="corewine")),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^lang/', set_language, name='set_lang'),
    url(r'^test/', set_lang, name='lang'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),
)
