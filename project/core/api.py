from django.conf.urls.defaults import patterns, url

from corewine import views as wine_views 
urlpatterns = patterns("",
	
    url(r'^teint/$',wine_views.TeintReadView.as_view(), name='teint'),

    url(r'^appelation/$',wine_views.AppelationCreateReadView.as_view(), name='appelation'),
 
    url(r'^cepage/$',wine_views.CepageCreateReadView.as_view(), name='cepage'),

    url(r'^country/$',wine_views.CountryCreateReadView.as_view(), name='country'),

    url(r'^producer/$',wine_views.ProducerCreateReadView.as_view(), name='producer'),

    url(r'^region/$',wine_views.RegionCreateReadView.as_view(), name='region'),

    url(r'^tag/$',wine_views.TagCreateReadView.as_view(), name='tag'),
)