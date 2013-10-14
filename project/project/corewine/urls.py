from django.conf.urls import patterns, url

from project.corewine.views import index, TastingView

# TODO: make sure urls are locale specific
urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^tasting/$', TastingView.as_view(), name='tasting'),
                       )
