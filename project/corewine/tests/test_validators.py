"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from corewine.models import *
from django.utils.translation import ugettext_lazy as _


class ValidatorsTest(TestCase):

	def test_non_numeric(self):
		# self.assertRaisesMessage(ValidationError,_('Expression should not contain numeric values'),validate_non_numeric,)
		self.assertRaisesMessage(ValidationError,_('Expression should not contain numeric values'),validate_non_numeric,'%^*(%%^')
		self.assertRaisesMessage(ValidationError,_('Expression should not contain numeric values'),validate_non_numeric,'179879878')
	
	def test_numeric_only(self):
		self.assertRaisesMessage(ValidationError,_('Expression should not contain numeric values'),validate_non_numeric,object)
		self.assertRaisesMessage(ValidationError,_('Expression should not contain numeric values'),validate_non_numeric,'aaaajk')
		self.assertRaisesMessage(ValidationError,_('Expression should not contain numeric values'),validate_non_numeric,'89089080954')


	# def test_float_string(self):
	# 	self.assertRaisesMessage(ValidationError,_('This is not a valid number'),validate_float_string,'1678698')

