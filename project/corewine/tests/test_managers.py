import json
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

import logging
from corewine.models import (
	Cepage,
	Wine,
	Region,
	Appelation,
	Country,
	Producer
)
logger = logging.getLogger('factory')
# DEBUGGING LOG
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)

from factories import *


class ApprovedManagerTests(TestCase):

		def test_cepage(self):
			cepage_a = CepageFactory.create(status='a')
			cepage_b = CepageFactory.create(status='r')
			cepage_c = CepageFactory.create(status='p')

			obj = Cepage.approved.all()
			self.assertQuerysetEqual(obj, ['<Cepage: '+ cepage_a.cepage+'>'])

		def test_region(self):
			region_a = RegionFactory.create(status='a')
			region_b = RegionFactory.create(status='r')
			region_c = RegionFactory.create(status='p')

			obj = Region.approved.all()
			self.assertQuerysetEqual(obj, ['<Region: '+ region_a.region+'>'])
			
			
		def test_appelation(self):
			appelation_a = AppelationFactory.create(status='a')
			appelation_b = AppelationFactory.create(status='r')
			appelation_c = AppelationFactory.create(status='p')

			obj = Appelation.approved.all()
			self.assertQuerysetEqual(obj, ['<Appelation: '+ appelation_a.appelation+'>'])


		def test_tag(self):
			tag_a = TagFactory.create(status='a')
			tag_b = TagFactory.create(status='r')
			tag_c = TagFactory.create(status='p')

			obj = Tag.approved.all()
			self.assertQuerysetEqual(obj, ['<Tag: '+ tag_a.tag+'>'])


		def test_country(self):
			country_a = CountryFactory.create(status='a')
			country_b = CountryFactory.create(status='r')
			country_c = CountryFactory.create(status='p')

			obj = Country.approved.all()
			self.assertQuerysetEqual(obj, ['<Country: '+ country_a.country+'>'])


		def test_producer(self):
			producer_a = ProducerFactory.create(status='a')
			producer_b = ProducerFactory.create(status='r')
			producer_c = ProducerFactory.create(status='p')

			obj = Producer.approved.all()
			self.assertQuerysetEqual(obj, ['<Producer: '+ producer_a.producer+'>'])