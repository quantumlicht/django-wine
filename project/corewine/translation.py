from modeltranslation.translator import translator, TranslationOptions
from corewine.models import Wine, Country, Aroma, Taste, Acidity, Tanin, Teint, Taste, Tag

class CountryTranslationOptions(TranslationOptions):
    fields = ('country',)

translator.register(Country, CountryTranslationOptions)