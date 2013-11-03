from django.conf.urls.defaults import patterns, url

from corewine import views as wine_views 
urlpatterns = patterns("",
	
    url(r'^teint/$',wine_views.TeintReadView.as_view(), name='teint'),
    
    url(r'^wine/$',wine_views.WineReadView.as_view(), name='wine'),

    url(r'^appelation/$',wine_views.AppelationReadView.as_view(), name='appelation'),
 
    url(r'^cepage/$',wine_views.CepageReadView.as_view(), name='cepage'),

    url(r'^country/$',wine_views.CountryReadView.as_view(), name='country'),

    url(r'^producer/$',wine_views.ProducerReadView.as_view(), name='producer'),

    url(r'^region/$',wine_views.RegionReadView.as_view(), name='region'),

    url(r'^tag/$',wine_views.TagReadView.as_view(), name='tag'),
)