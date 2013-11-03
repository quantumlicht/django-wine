from django.test import TestCase
from corewine.views import *
from corewine.models import * 
from django.core.urlresolvers import reverse
import json
import logging

log = logging.getLogger(__name__)


class ApiTests(TestCase):

	def setUp(self):
		Cepage.objects.get_or_create(cepage='test_cepage_1', status='a')
		Cepage.objects.get_or_create(cepage='test_cepage_2', status='a')

		self.create_read_cepage_url = reverse("api:cepage")
		self.form_url = reverse('corewine:tasting')
		self.client.login(username='test_user', password='123456')

	# def test_create(self):
	# 	post = {'cepage': 'test_cepage_3', 'status':'p'}
	# 	response = self.client.post(self.create_read_cepage_url, post, follow=True)
	# 	print response.status_code
	# 	data = json.loads(response.content)
	# 	self.assertEquals(response.status_code, 201)
	# 	content = {'id':3, 'cepage': 'test_cepage_3', 'status':'p'}
	# 	self.assertEquals(data,content)
	# 	self.assertEquals(Cepage.objects.count(),3)






class ViewTests(TestCase):

	def setUp(self):
		self.index_url = reverse('landing')


	def test_index(self):
		response = self.client.get(self.index_url)
		self.assertEquals(response.status_code,200)


