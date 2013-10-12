from django.conf.urls import patterns, url

from project.corewine import views

# TODO: make sure urls are locale specific
urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^tasting/$', views.tasting, name='tasting'),
                       )
