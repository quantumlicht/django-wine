from modeltranslation.translator import translator, TranslationOptions
from corewine.models import Wine, Country, Aroma, Taste, Acidity, Tanin, Teint, Tag, Appelation, Region

class CountryTranslationOptions(TranslationOptions):
    fields = ('country',)


class AcidityTranslationOptions(TranslationOptions):
	fields = ('acidity',)


class AromaTranslationOptions(TranslationOptions):
	fields = ('aroma',)


class TasteTranslationOptions(TranslationOptions):
	fields = ('taste',)


class TaninTranslationOptions(TranslationOptions):
	fields = ('tanin',)


class TagTranslationOptions(TranslationOptions):
	fields = ('tag','description')


class RegionTranslationOptions(TranslationOptions):
	fields = ('region',)


class TeintTranslationOptions(TranslationOptions):
	fields = ('teint',)


class AppelationTranslationOptions(TranslationOptions):
	fields = ('appelation',)


translator.register(Country, CountryTranslationOptions)
translator.register(Acidity, AcidityTranslationOptions)
translator.register(Aroma, AromaTranslationOptions)
translator.register(Taste, TasteTranslationOptions)
translator.register(Tanin, TaninTranslationOptions)
translator.register(Teint, TeintTranslationOptions)
translator.register(Appelation, AppelationTranslationOptions)
translator.register(Region, RegionTranslationOptions)
translator.register(Tag, TagTranslationOptions)