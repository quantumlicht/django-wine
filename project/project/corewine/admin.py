from django.contrib import admin
from project.corewine.models import *


class CepageInline(admin.TabularInline):
    model = Wine.cepage.through


class WineAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Fiche', {
            'fields': (
                ('name', 'producer', 'year'),
                'appelation',
                ('region', 'country'),
                'cepage',
                'date',
                ('code_saq','alcool', 'price')
            )
        }),
        ('Eye', {
           'fields': ('wineType', 'teint')
        }),
        ('Nose', {
            'fields': ('nose_intensity', 'aroma')
        }),
        ('Mouth', {
            'fields': ('mouth_intensity', 'persistance', 'taste', 'acidity', 'tanin')
        })
    )


class TagAdmin(admin.ModelAdmin):
    list_display = ['tag', 'wineType', 'is_approved']
    list_filter = ['status']

class CepageAdmin(admin.ModelAdmin):
    list_display = ['cepage', 'wineType', 'is_approved']
    list_filter = ['status']


admin.site.register(Wine, WineAdmin)
admin.site.register(Cepage, CepageAdmin)
admin.site.register(Aroma)
admin.site.register(Acidity)
admin.site.register(Tag, TagAdmin)
