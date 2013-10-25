"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.core.exceptions import ValidationError
from django.test import TestCase
import core.validators as v
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from corewine.models import Wine



class CharFieldForm(ModelForm):
	model = Wine
	fields = ('name', 'producer', 'appelation', 'region', 'code_saq', 'tag', 'cepage')


class PriceFieldForm(ModelForm):
	model = Wine
	fields = ('price')


class ValidatorsTest(TestCase):

	def get_price(self, arg):
		wine = Wine(price=arg)
		f = PriceFieldForm(instance=wine)
		return f.errors

	def test_price(self):
		test_a = self.get_price('aaaaaaaa')
		self.assertEqual(test_a, 'a')


		test_b = self.get_price(11.111111)
		self.assertEqual(test_b, False)







	def test_charfields(self):
		# self.assertRaisesMessage(ValidationError,_('Expression should not contain numeric values'),validate_non_numeric,)
		self.assertRaisesMessage(ValidationError,_('Expression should not contain numeric values'),v.validate_non_numeric,'%^*(%%^')
		self.assertRaisesMessage(ValidationError,_('Expression should not contain numeric values'),v.validate_non_numeric,'179879878')
	
	def test_numeric_only(self):
		self.assertRaisesMessage(ValidationError,_('Expression should not contain numeric values'),v.validate_non_numeric,object)
		# self.assertRaisesMessage(ValidationError,_('Expression should not contain numeric values'),v.validate_non_numeric,'aaaajk')


	# def test_float_string(self):
	# 	self.assertRaisesMessage(ValidationError,_('This is not a valid number'),validate_float_string,'1678698')

