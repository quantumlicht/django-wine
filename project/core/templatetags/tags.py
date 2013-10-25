from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.filter(name='class_name')
def class_name(ob):
    return ob.__class__.__name__

#from: http://gnuvince.wordpress.com/2007/09/14/a-django-template-tag-for-the-current-active-page/
@register.simple_tag
def active(request, urls):
    if request.path in (reverse(url) for url in urls.split() ):
        return 'active'
    return ''