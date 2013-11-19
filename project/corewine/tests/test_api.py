import json
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

import logging
logger = logging.getLogger('factory')
# DEBUGGING LOG
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)


from factories import *
	

# ============================================================================================
# TESTS
# ============================================================================================
class ApiTests(TestCase):

	def setUp(self):
		self.wine_url = reverse('api:wine')
		self.appelation_url = reverse('api:appelation')
		self.cepage_url = reverse('api:cepage')
		self.country_url = reverse('api:country')
		self.producer_url = reverse('api:producer')
		self.region_url = reverse('api:region')
		self.tag_url = reverse('api:tag')
		self.teint_url = reverse('api:teint')
	
	# =======================================================================================
	# CEPAGE API
	# =======================================================================================
	def test_cepage_with_pending(self):
		cepage_a = CepageFactory.create()
		cepage_b = CepageFactory.create()
		response = self.client.get(self.cepage_url)
		
		self.assertEquals(response.status_code,200)

		self.assertNotContains(response,cepage_a)
		self.assertNotContains(response,cepage_b)


	def test_cepage_with_approved(self):
		cepage_a = CepageFactory.create(status='a')
		cepage_b = CepageFactory.create(status='a')

		response = self.client.get(self.cepage_url)
		
		self.assertEquals(response.status_code,200)

		self.assertContains(response,cepage_a)
		self.assertContains(response,cepage_b)


	def test_cepage_with_rejected(self):
		cepage_a = CepageFactory.create(status='r')
		cepage_b = CepageFactory.create(status='r')

		response = self.client.get(self.cepage_url)
		
		self.assertEquals(response.status_code,200)

		self.assertNotContains(response,cepage_a)
		self.assertNotContains(response,cepage_b)


	def test_cepage_with_mix(self):
		cepage_a = CepageFactory.create(status='a')
		cepage_b = CepageFactory.create(status='p')

		response = self.client.get(self.cepage_url)
		
		self.assertEquals(response.status_code,200)

		self.assertContains(response,cepage_a)
		self.assertNotContains(response,cepage_b)

	# =======================================================================================
	# APPELATION API
	# =======================================================================================
	def test_appelation_with_pending(self):
		appelation_a = AppelationFactory.create()
		appelation_b = AppelationFactory.create()
		response = self.client.get(self.appelation_url)
		
		self.assertEquals(response.status_code,200)

		self.assertNotContains(response,appelation_a)
		self.assertNotContains(response,appelation_b)


	def test_appelation_with_approved(self):
		appelation_a = AppelationFactory.create(status='a')
		appelation_b = AppelationFactory.create(status='a')

		response = self.client.get(self.appelation_url)
		
		self.assertEquals(response.status_code,200)

		self.assertContains(response,appelation_a)
		self.assertContains(response,appelation_b)


	def test_appelation_with_rejected(self):
		appelation_a = AppelationFactory.create(status='r')
		appelation_b = AppelationFactory.create(status='r')

		response = self.client.get(self.appelation_url)
		
		self.assertEquals(response.status_code,200)

		self.assertNotContains(response,appelation_a)
		self.assertNotContains(response,appelation_b)


	def test_appelation_with_mix(self):
		appelation_a = AppelationFactory.create(status='a')
		appelation_b = AppelationFactory.create(status='p')

		response = self.client.get(self.appelation_url)
		
		self.assertEquals(response.status_code,200)

		self.assertContains(response,appelation_a)
		self.assertNotContains(response,appelation_b)

	# =======================================================================================
	# COUNTRY API
	# =======================================================================================
	def test_country_with_pending(self):
		country_a = CountryFactory.create()
		country_b = CountryFactory.create()
		response = self.client.get(self.country_url)
		
		self.assertEquals(response.status_code,200)

		self.assertNotContains(response,country_a)
		self.assertNotContains(response,country_b)


	def test_country_with_approved(self):
		country_a = CountryFactory.create(status='a')
		country_b = CountryFactory.create(status='a')

		response = self.client.get(self.country_url)
		
		self.assertEquals(response.status_code,200)

		self.assertContains(response,country_a)
		self.assertContains(response,country_b)


	def test_country_with_rejected(self):
		country_a = CountryFactory.create(status='r')
		country_b = CountryFactory.create(status='r')

		response = self.client.get(self.country_url)
		
		self.assertEquals(response.status_code,200)

		self.assertNotContains(response,country_a)
		self.assertNotContains(response,country_b)


	def test_country_with_mix(self):
		country_a = CountryFactory.create(status='a')
		country_b = CountryFactory.create(status='p')

		response = self.client.get(self.country_url)
		
		self.assertEquals(response.status_code,200)

		self.assertContains(response,country_a)
		self.assertNotContains(response,country_b)

	# =======================================================================================
	# PRODUCER API
	# =======================================================================================
	def test_producer_with_pending(self):
		producer_a = ProducerFactory.create()
		producer_b = ProducerFactory.create()
		response = self.client.get(self.producer_url)
		
		self.assertEquals(response.status_code,200)

		self.assertNotContains(response,producer_a)
		self.assertNotContains(response,producer_b)


	def test_producer_with_approved(self):
		producer_a = ProducerFactory.create(status='a')
		producer_b = ProducerFactory.create(status='a')

		response = self.client.get(self.producer_url)
		
		self.assertEquals(response.status_code,200)

		self.assertContains(response,producer_a)
		self.assertContains(response,producer_b)


	def test_producer_with_rejected(self):
		producer_a = ProducerFactory.create(status='r')
		producer_b = ProducerFactory.create(status='r')

		response = self.client.get(self.producer_url)
		
		self.assertEquals(response.status_code,200)

		self.assertNotContains(response,producer_a)
		self.assertNotContains(response,producer_b)


	def test_producer_with_mix(self):
		producer_a = ProducerFactory.create(status='a')
		producer_b = ProducerFactory.create(status='p')

		response = self.client.get(self.producer_url)
		
		self.assertEquals(response.status_code,200)

		self.assertContains(response,producer_a)
		self.assertNotContains(response,producer_b)

	# =======================================================================================
	# REGION API
	# =======================================================================================
	def test_region_with_pending(self):
		region_a = RegionFactory.create()
		region_b = RegionFactory.create()
		response = self.client.get(self.region_url)
		
		self.assertEquals(response.status_code,200)

		self.assertNotContains(response,region_a)
		self.assertNotContains(response,region_b)


	def test_region_with_approved(self):
		region_a = RegionFactory.create(status='a')
		region_b = RegionFactory.create(status='a')

		response = self.client.get(self.region_url)
		
		self.assertEquals(response.status_code,200)

		self.assertContains(response,region_a)
		self.assertContains(response,region_b)


	def test_region_with_rejected(self):
		region_a = RegionFactory.create(status='r')
		region_b = RegionFactory.create(status='r')

		response = self.client.get(self.region_url)
		
		self.assertEquals(response.status_code,200)

		self.assertNotContains(response,region_a)
		self.assertNotContains(response,region_b)


	def test_region_with_mix(self):
		region_a = RegionFactory.create(status='a')
		region_b = RegionFactory.create(status='p')

		response = self.client.get(self.region_url)
		
		self.assertEquals(response.status_code,200)

		self.assertContains(response,region_a)
		self.assertNotContains(response,region_b)

	# =======================================================================================
	# TAG API
	# =======================================================================================
	def test_tag_with_pending(self):
		tag_a = TagFactory.create()
		tag_b = TagFactory.create()
		response = self.client.get(self.tag_url)
		
		self.assertEquals(response.status_code,200)

		self.assertNotContains(response,tag_a)
		self.assertNotContains(response,tag_b)


	def test_tag_with_approved(self):
		tag_a = TagFactory.create(status='a')
		tag_b = TagFactory.create(status='a')

		response = self.client.get(self.tag_url)
		
		self.assertEquals(response.status_code,200)

		self.assertContains(response,tag_a)
		self.assertContains(response,tag_b)


	def test_tag_with_rejected(self):
		tag_a = TagFactory.create(status='r')
		tag_b = TagFactory.create(status='r')

		response = self.client.get(self.tag_url)
		
		self.assertEquals(response.status_code,200)

		self.assertNotContains(response,tag_a)
		self.assertNotContains(response,tag_b)


	def test_tag_with_mix(self):
		tag_a = TagFactory.create(status='a')
		tag_b = TagFactory.create(status='p')

		response = self.client.get(self.tag_url)
		
		self.assertEquals(response.status_code,200)

		self.assertContains(response,tag_a)
		self.assertNotContains(response,tag_b)

	# =======================================================================================
	# TEINT API
	# =======================================================================================
	def test_teint_with_red_wine_query_white(self):
		teint_a = TeintFactory.create(wineType='r')
		teint_b = TeintFactory.create(wineType='r')

		response = self.client.get(self.teint_url,{'type':'w'})
		self.assertEquals(response.status_code,200)
		self.assertEquals(response.content,'[]')


	def test_teint_with_red_wine_query_red(self):
		teint_a = TeintFactory.create(wineType='r')
		teint_b = TeintFactory.create(wineType='r')

		response = self.client.get(self.teint_url,{'type':'r'})
		self.assertEquals(response.status_code,200)

		self.assertContains(response,teint_a)
		self.assertContains(response,teint_b)


	def test_teint_with_red_wine_query_invalid(self):
		teint_a = TeintFactory.create(wineType='r')
		teint_b = TeintFactory.create(wineType='r')

		response = self.client.get(self.teint_url,{'type':'invalid_type'})
		self.assertEquals(response.status_code,200)
		self.assertEquals(response.content,'[]')

		response = self.client.get(self.teint_url,{'type':789789})
		self.assertEquals(response.status_code,200)
		self.assertEquals(response.content,'[]')


	def test_teint_with_mix(self):
		teint_a = TeintFactory.create(wineType='r')
		teint_b = TeintFactory.create(wineType='w')

		response = self.client.get(self.teint_url,{'type':'r'})
		self.assertEquals(response.status_code,200)
		self.assertContains(response,teint_a)
		self.assertNotContains(response,teint_b)

		response = self.client.get(self.teint_url,{'type':'w'})
		self.assertEquals(response.status_code,200)
		self.assertNotContains(response,teint_a)
		self.assertContains(response,teint_b)


	def test_teint_with_white_wine_query_red(self):
		teint_a = TeintFactory.create(wineType='w')
		teint_b = TeintFactory.create(wineType='w')

		response = self.client.get(self.teint_url,{'type':'r'})
		self.assertEquals(response.status_code,200)
		self.assertEquals(response.content,'[]')


	def test_teint_with_white_wine_query_white(self):
		teint_a = TeintFactory.create(wineType='w')
		teint_b = TeintFactory.create(wineType='w')

		response = self.client.get(self.teint_url,{'type':'w'})
		self.assertEquals(response.status_code,200)
		self.assertContains(response,teint_a)
		self.assertContains(response,teint_b)


	def test_teint_with_white_wine_query_invalid(self):
		teint_a = TeintFactory.create(wineType='w')
		teint_b = TeintFactory.create(wineType='w')

		response = self.client.get(self.teint_url,{'type':'invalid_type'})
		self.assertEquals(response.status_code,200)
		self.assertEquals(response.content,'[]')

		response = self.client.get(self.teint_url,{'type':789789})
		self.assertEquals(response.status_code,200)
		self.assertEquals(response.content,'[]')

	# =======================================================================================
	# WINE API
	# =======================================================================================
	def test_wine_with_good_wine(self):
		wine_a = WineFactory.create(name=u'wine a')
		wine_b = WineFactory.create(name=u'wine b')

		response = self.client.get(self.wine_url,{'name':'wine b'})
		data = json.loads(response.content)
		self.assertEquals(response.status_code,200)
		self.assertEquals(len(data),1) # Creation makes name as title
		self.assertEquals(data[0]['name'],'Wine B')


	def test_wine_with_bad_request(self):
		wine_a = WineFactory.create(name=u'wine a')
		wine_b = WineFactory.create(name=u'wine b')

		response = self.client.get(self.wine_url,{'name':'bad request'})
		data = json.loads(response.content)
		self.assertEquals(response.status_code,200)
		self.assertEquals(data,[])

	def test_wine_with_bad_numeric_request(self):
		wine_a = WineFactory.create(name=u'wine a')
		wine_b = WineFactory.create(name=u'wine b')

		response = self.client.get(self.wine_url,{'name':78998789})
		data = json.loads(response.content)
		self.assertEquals(response.status_code,200)
		self.assertEquals(data,[])