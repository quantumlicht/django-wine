from django.conf.urls import patterns, url

from .views import index, WineCreateView, WineListView, WineDetailView

# TODO: make sure urls are locale specific
urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^tasting/$', WineCreateView.as_view(), name='tasting'),
                       url(r'^wine_list/$', WineListView.as_view(), name='list'),
                       url(r'^wine_list/(?P<pk>\d+)/$', WineDetailView.as_view(), name='detail'),
                       )
