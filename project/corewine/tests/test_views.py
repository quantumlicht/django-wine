from django.test import TestCase
from corewine.views import *
from corewine.models import * 
from django.core.urlresolvers import reverse
import factory
from factory.fuzzy import FuzzyText
import json
import logging

log = logging.getLogger(__name__)

class WineFactory(factory.Factory):
	FACTORY_FOR = Wine

	name = FuzzyText()
	producer = FuzzyText()
	producer = FuzzyText()
	producer = FuzzyText()
	producer = FuzzyText()



class ApiTests(TestCase):

	def setUp(self):
		Cepage.objects.get_or_create(cepage='test_cepage_1', status='a')
		Cepage.objects.get_or_create(cepage='test_cepage_2', status='a')
		self.create_read_cepage_url = reverse("api:cepage")
		self.form_url = reverse('corewine:tasting')
		
		self.client.login(username='test_user', password='123456')


class TaninTests(TestCase):
	def test_create(self):
		mommy.make(Tanin, _quantity=3)
		tanins = Tanin.objects.all()
		self.assertEquals(len(tanins),3)


class ViewTests(TestCase):

	def setUp(self):
		self.tanin_recipe = Recipe(Tanin,

			)
		self.index_url = reverse('landing')
		self.list_url = reverse('corewine:list')

	def test_index(self):
		response = self.client.get(self.index_url)
		self.assertEquals(response.status_code,200)

	# def test_wine_list(self):
	# 	tanin = mommy.make(Tanin)
	# 	response = self.client.get(self.list_url)
	# 	self.assertContains(response, 'test_1')

