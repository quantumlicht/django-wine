import factory
from datetime import datetime
from factory import fuzzy
from corewine.models import (
	Wine,
	Cepage,
	Appelation,
	Country,
	Producer,
	Region,
	Tag,
	Teint,
	Aroma,
	Taste,
	Acidity,
	Tanin
)

class CepageFactory(factory.django.DjangoModelFactory):
	FACTORY_FOR = Cepage
	cepage = fuzzy.FuzzyText()
	status = 'p'
	wineType = 'w'


class AromaFactory(factory.django.DjangoModelFactory):
	FACTORY_FOR = Aroma
	order = 1
	aroma = fuzzy.FuzzyText()


class TaninFactory(factory.django.DjangoModelFactory):
	FACTORY_FOR = Tanin
	order = 1
	tanin = fuzzy.FuzzyText()


class TasteFactory(factory.django.DjangoModelFactory):
	FACTORY_FOR = Taste
	order = 1
	taste = fuzzy.FuzzyText()


class AcidityFactory(factory.django.DjangoModelFactory):
	FACTORY_FOR = Acidity
	order = 1
	acidity = fuzzy.FuzzyText()


class AppelationFactory(factory.django.DjangoModelFactory):
	FACTORY_FOR = Appelation
	appelation = fuzzy.FuzzyText()
	status = 'p'


class CountryFactory(factory.django.DjangoModelFactory):
	FACTORY_FOR = Country
	country = fuzzy.FuzzyText()
	status = 'p'


class ProducerFactory(factory.django.DjangoModelFactory):
	FACTORY_FOR = Producer
	producer = fuzzy.FuzzyText()
	status = 'p'


class RegionFactory(factory.django.DjangoModelFactory):
	FACTORY_FOR = Region
	region = fuzzy.FuzzyText()
	status = 'p'


class TagFactory(factory.django.DjangoModelFactory):
	FACTORY_FOR = Tag
	tag = fuzzy.FuzzyText()
	description = fuzzy.FuzzyText()
	status = 'p'


class TeintFactory(factory.django.DjangoModelFactory):
	FACTORY_FOR = Teint
	wineType = 'w'
	teint = fuzzy.FuzzyText()
	order = fuzzy.FuzzyInteger(1,10)


class WineFactory(factory.django.DjangoModelFactory):
	FACTORY_FOR = Wine
	wineType = 'w'
	name = u'test'
	# cepage = factory.SubFactory(CepageFactory)
	appelation = factory.SubFactory(AppelationFactory)
	country = factory.SubFactory(CountryFactory)
	producer = factory.SubFactory(ProducerFactory)
	region = factory.SubFactory(RegionFactory)
	# tag = factory.SubFactory(TagFactory)
	teint = factory.SubFactory(TeintFactory)
	# slug = u'slug-a'
	date = fuzzy.FuzzyDate(datetime(2005,1,1).date())
	alcool = fuzzy.FuzzyDecimal(1,100)
	price = fuzzy.FuzzyDecimal(1,1000)
	year = 2009
	mouth_intensity = 0.5
	nose_intensity = 0.5
	rating = 0.5
	persistance = 0.5
	aroma = factory.SubFactory(AromaFactory)
	taste = factory.SubFactory(TasteFactory)
	acidity = factory.SubFactory(AcidityFactory)
	tanin = factory.SubFactory(TaninFactory)
	code_saq = fuzzy.FuzzyInteger(0,10000000)
