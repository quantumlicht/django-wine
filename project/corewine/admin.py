from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import ugettext_lazy as _
from .models import *


# ==================================================
#  ADMIN ACTIONS
# ==================================================

def make_approved(modeladmin, request, queryset):
    queryset.update(status='a')
make_approved.short_description = _("Mark selected as approved")


def make_rejected(modeladmin, request, queryset):
    queryset.update(status='r')
make_rejected.short_description = _("Mark selected as rejected")

def make_red(modeladmin, request, queryset):
        queryset.update(wineType='r')
make_red.short_description = _("Mark selected as Red")

def make_white(modeladmin, request, queryset):
        queryset.update(wineType='w')
make_white.short_description = _("Mark selected as White")

def make_none(modeladmin,request,queryset):
    queryset.update(wineType='n')
make_none.short_description = _("Mark selected as None")

# ==================================================
#  STYLING CLASSES
# ==================================================

class CepageInline(admin.TabularInline):
    model = Wine.cepage.through


# ==================================================
#  ADMIN CLASSES
# ==================================================

# -------------------------------------------
class AcidityAdmin(TranslationAdmin):
    """ 
    Manage the Acidity fields
    """
    fields = ('acidity', 'order')
    list_display = ['acidity_fr','acidity_en', 'order', 'last_modified', 'created']
    ordering = ['order']


# -------------------------------------------
class AppelationAdmin(TranslationAdmin):
    fields =('appelation', 'status')
    list_display = ['appelation_fr','appelation_en','is_approved', 'last_modified', 'created']
    ordering = ['status']
    actions = [make_rejected, make_approved]


# -------------------------------------------
class AromaAdmin(TranslationAdmin):
    """ Manage the Aroma fields """
    fields = ('aroma', 'order')
    list_display = ['aroma_fr','aroma_en', 'order', 'last_modified', 'created']
    ordering = ['order']


# -------------------------------------------
class CepageAdmin(admin.ModelAdmin):
    list_display = ['cepage', 'wineType', 'is_approved', 'last_modified', 'created']
    list_filter = ['status']
    actions = [make_rejected, make_approved, make_red, make_white]


# -------------------------------------------
class CountryAdmin(TranslationAdmin):
    """ Manage Countries """
    fields = ('country', 'status')
    list_display = ['country_fr','country_en','is_approved', 'last_modified', 'created']
    list_filter = ['status']
    actions = [make_rejected, make_approved]


# -------------------------------------------
class ProducerAdmin(admin.ModelAdmin):
    fields =('producer', 'status')
    list_display = ('producer', 'is_approved', 'last_modified', 'created')
    ordering = ['status']
    list_filter = ['status']
    actions = [make_rejected, make_approved]

# -------------------------------------------
class RegionAdmin(TranslationAdmin):
    fields =('region', 'status')
    list_display = ('region_fr', 'region_en', 'is_approved', 'last_modified', 'created')
    ordering = ['status']
    list_filter = ['status']
    actions = [make_rejected, make_approved]


# -------------------------------------------
class TeintAdmin(TranslationAdmin):
    """ Manage the Teint fields """
    fields = ('teint', 'wineType', 'order')
    list_display = ['teint_fr','teint_en', 'wineType', 'order', 'last_modified', 'created']
    list_filter = ['wineType']    
    ordering = ['wineType', 'order']
    actions = [make_red, make_white]

# -------------------------------------------
class TasteAdmin(TranslationAdmin):
    """ Manage the Taste fields """
    fields = ('taste', 'order')
    list_display = ['taste_fr','taste_en', 'order', 'last_modified', 'created']
    list_filter = ['taste']    
    ordering = ['order']
    actions = [make_red, make_white]


# -------------------------------------------
class WineAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('wineType','name','year')}
    list_display = ['name', 'wineType', 'producer', 'appelation', 'list_cepage', 'region', 'country', 'year','code_saq', 'price', 'alcool','rating']
    list_filter = ['producer','wineType', 'country', 'cepage', 'region','appelation']
    search_fields = ['name','producer','appelation','cepage','region','code_saq']
    fieldsets = (
        ('Fiche', {
            'fields': (
                ('name', 'slug', 'producer', 'year'),
                ('appelation','region', 'country'),
                ('cepage','tag'),
                ('date','code_saq', 'alcool', 'price', 'rating'),
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
        }),
    )


# -------------------------------------------
class TaninAdmin(TranslationAdmin):
    list_display = ['tanin_fr', 'tanin_en', 'order', 'last_modified', 'created']
    list_filter = ['tanin']
    ordering = ['order']


# -------------------------------------------
class TagAdmin(TranslationAdmin):
    list_display = ['tag_fr', 'tag_en', 'description_fr', 'description_en', 'wineType', 'is_approved', 'last_modified', 'created']
    list_filter = ['status', 'wineType', 'last_modified']
    actions = [make_rejected, make_approved, make_red, make_white, make_none]



# ==================================================
#  ADMIN REGISTRATION
# ==================================================

admin.site.register(Acidity, AcidityAdmin)

admin.site.register(Appelation, AppelationAdmin)

admin.site.register(Aroma, AromaAdmin)

admin.site.register(Cepage, CepageAdmin)

admin.site.register(Country, CountryAdmin)

admin.site.register(Producer, ProducerAdmin)

admin.site.register(Region, RegionAdmin)

admin.site.register(Tag, TagAdmin)

admin.site.register(Tanin, TaninAdmin)

admin.site.register(Taste, TasteAdmin)

admin.site.register(Teint, TeintAdmin)

admin.site.register(Wine, WineAdmin)
