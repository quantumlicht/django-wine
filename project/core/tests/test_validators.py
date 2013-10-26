"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.core.exceptions import ValidationError
from django.test import TestCase
import core.validators as v
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, Form
from django import forms
from corewine.models import Wine



class CharFieldForm(ModelForm):
	model = Wine
	fields = ('name', 'producer', 'appelation', 'region', 'code_saq', 'tag', 'cepage')


class PriceFieldForm(Form):
	price = forms.FloatField(validators=[v.price])


class ValidatorsTest(TestCase):

	def get_price(self, price):
		# wine = Wine(price=arg)
		f = PriceFieldForm({'price': price})
		return f.errors['price']

	def test_price(self):
	
		test = PriceFieldForm({'price': 00000000.000000000000}).errors
		self.assertEqual({}, test)

		test = PriceFieldForm({'price': 111.11}).errors
		self.assertEqual({}, test)

		test = self.get_price(111.1111)
		self.assertIn(v.price.message.format(), test)

		test = self.get_price('')
		self.assertIn(_(u'This field is required.'),test)

		test = self.get_price('aaaa')
		self.assertIn(_(u'Enter a number.'),test)

		test = self.get_price(object)
		self.assertIn(_(u'Enter a number.'),test)








	def test_charfields(self):
		# self.assertRaisesMessage(ValidationError,_('Expression should not contain numeric values'),non_numeric,)
		self.assertRaisesMessage(ValidationError,_('Expression should not contain numeric values'),v.non_numeric,'%^*(%%^')
		self.assertRaisesMessage(ValidationError,_('Expression should not contain numeric values'),v.non_numeric,'179879878')
	
	def test_numeric_only(self):
		self.assertRaisesMessage(ValidationError,_('Expression should not contain numeric values'),v.non_numeric,object)
		# self.assertRaisesMessage(ValidationError,_('Expression should not contain numeric values'),v.non_numeric,'aaaajk')


	# def test_float_string(self):
	# 	self.assertRaisesMessage(ValidationError,_('This is not a valid number'),float_string,'1678698')

