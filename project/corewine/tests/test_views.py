from django.test import TestCase
from corewine.models import * 
from django.core.urlresolvers import reverse
import json
import logging

log = logging.getLogger(__name__)

from factories import *


class ViewTests(TestCase):

	def setUp(self):
		self.index_url = reverse('corewine:index')
		self.wine_list_url = reverse('corewine:list')
		self.client.login(username='test_user', password='123456')

	def test_index(self):
		response = self.client.get(self.index_url)
		self.assertEquals(response.status_code,200)

	def test_winelist(self):
		wine_a = WineFactory.create(name=u'wine a')
		wine_b = WineFactory.create(name=u'wine b')

		response = self.client.get(self.wine_list_url)
		self.assertEquals(response.status_code,200)

		self.assertContains(response, wine_a.name)
		self.assertContains(response, wine_b.name)

	def test_detail(self):
		wine_a = WineFactory.create(name=u'wine a')
		wine_b = WineFactory.create(name=u'wine b')
		response = self.client.get(reverse('corewine:detail',kwargs={'slug':wine_a.slug}))
		self.assertEquals(response.status_code,200)

		self.assertContains(response, wine_a.name)
		self.assertContains(response, wine_a.country)

