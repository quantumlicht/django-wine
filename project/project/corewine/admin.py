from django.contrib import admin
from project.corewine.models import *


class AcidityAdmin(admin.ModelAdmin):
    """Manage the Acidity fields """
    fields = ('acidity', 'order')
    list_display = ['acidity', 'order']


class AromaAdmin(admin.ModelAdmin):
    """ Manage the Aroma fields """
    fields = ('aroma', 'order')
    list_display = ['aroma', 'order']


class CepageInline(admin.TabularInline):
    model = Wine.cepage.through


class TeintAdmin(admin.ModelAdmin):
    """Manage the Teint fields"""
    fields = ('teint', 'wineType', 'order')
    list_display = ['teint', 'wineType', 'order']
    list_filter = ['wineType']    

class TasteAdmin(admin.ModelAdmin):
    """Manage the Taste fields"""
    fields = ('taste', 'order')
    list_display = ['taste', 'order']
    list_filter = ['taste']    


class WineAdmin(admin.ModelAdmin):
    # date_hierarchy = 'last_modified'
    list_display = ['name', 'wineType', 'producer', 'appelation', 'list_cepage', 'region', 'country', 'year','code_saq', 'price', 'alcool','rating']
    list_filter = ['producer','wineType', 'country', 'cepage', 'region','appelation']
    search_fields = ['name','producer','appelation','cepage','region','code_saq']
    fieldsets = (
        ('Fiche', {
            'fields': (
                ('name', 'producer', 'year'),
                'appelation',
                ('region', 'country'),
                'cepage',
                'date',
                ('code_saq', 'alcool', 'price'),
                'rating',
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

class TaninAdmin(admin.ModelAdmin):
    list_display = ['tanin','order',]
    list_filter = ['tanin']



class TagAdmin(admin.ModelAdmin):
    list_display = ['tag', 'wineType', 'is_approved', 'last_modified']
    list_filter = ['status']


class CepageAdmin(admin.ModelAdmin):
    list_display = ['cepage', 'wineType', 'is_approved']
    list_filter = ['status']


admin.site.register(Wine, WineAdmin)
admin.site.register(Tanin,TaninAdmin)
admin.site.register(Cepage, CepageAdmin)
admin.site.register(Aroma, AromaAdmin)
admin.site.register(Acidity, AcidityAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Taste, TasteAdmin)
admin.site.register(Teint, TeintAdmin)
