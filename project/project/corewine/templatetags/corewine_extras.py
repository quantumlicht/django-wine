from django import template

register = template.Library()

@register.filter(name='class_name')
def class_name(ob):
    return ob.__class__.__name__