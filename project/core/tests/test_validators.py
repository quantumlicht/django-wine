# -*- coding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.core.exceptions import ValidationError
from django.test import TestCase
import core.validators as v
from django.utils import timezone
from datetime import datetime,timedelta
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as ugettext

import logging

log = logging.getLogger(__name__)


class ValidatorsTest(TestCase):
	# =======================================================================================
	# FUTURE_DATE VALIDATOR
	# =======================================================================================
	def test_future_date_with_present_date(self):
		self.assertEquals(None, v.validate_future_date(datetime.now().date()))


	def test_future_date_with_past_date(self):
		self.assertEquals(None, v.validate_future_date(datetime.now().date() + timedelta(days=-30)))


	def test_future_date_with_future_date(self):
		self.assertRaisesMessage(ValidationError,_('Invalid Date. This date is in the future.'),v.validate_future_date, datetime.now().date()+timedelta(days=30))
		with self.assertRaises(ValidationError) as e:
			v.validate_future_date(datetime.now().date()+timedelta(days=30))
		exc  = e.exception
		self.assertEqual(exc.code, 'invalid_date')

	# =======================================================================================
	# PERCENTAGE VALIDATOR
	# =======================================================================================
	def test_percentage_with_string_correct_percentage(self):
		self.assertEquals(None, v.percentage('46.78'))
		self.assertEquals(None, v.percentage('45.1'))
		self.assertEquals(None, v.percentage('45'))


	def test_percentage_with_float_correct_percentage(self):
		self.assertEquals(None, v.percentage(46.78))
		self.assertEquals(None, v.percentage(45.1))
		self.assertEquals(None, v.percentage(45))


	def test_percentage_with_string_percentage_sign(self):
		# self.assertRaisesMessage(ValidationError,_('This is not a valid percentage. Maximum is 100% and only put 2 decimals maximum.'),v.percentage, '12.78%')
		with self.assertRaises(ValidationError) as e:
			v.percentage('12.78%')
		exc  = e.exception
		self.assertEqual(exc.code, 'not_percentage')


	def test_percentage_with_string_many_decimals(self):
		# self.assertRaisesMessage(ValidationError,_('This is not a valid percentage. Maximum is 100% and only put 2 decimals maximum.'),v.percentage, '12.788888')
		with self.assertRaises(ValidationError) as e:
			v.percentage('12.788888')
		exc  = e.exception
		self.assertEqual(exc.code, 'not_percentage')


	def test_percentage_with_float_many_decimals(self):
		# self.assertRaisesMessage(ValidationError,_('This is not a valid percentage. Maximum is 100% and only put 2 decimals maximum.'),v.percentage, 12.788888)
		with self.assertRaises(ValidationError) as e:
			v.percentage(12.788888)
		exc  = e.exception
		self.assertEqual(exc.code, 'not_percentage')

	def test_percentage_with_object(self):
		# self.assertRaisesMessage(ValidationError,_('This is not a valid percentage. Maximum is 100% and only put 2 decimals maximum.'),v.percentage, object)
		with self.assertRaises(ValidationError) as e:
			v.percentage(object)
		exc  = e.exception
		self.assertEqual(exc.code, 'not_percentage')

	# =======================================================================================
	# PRICE VALIDATOR
	# =======================================================================================
	def test_price_with_numeric_string_correct_decimals(self):
		self.assertEquals(None, v.price('1246.78'))
		self.assertEquals(None, v.price('1245.34'))
		self.assertEquals(None, v.price('12431'))


	def test_price_with_numeric_string_with_dollar_sign(self):
		# self.assertRaisesMessage(ValidationError,_('Not a valid price. 2 decimals maximum and numbers only is allowed.'),v.price, '1246.78$')
		with self.assertRaises(ValidationError) as e:
			v.price('1246.78$')
		exc  = e.exception
		self.assertEqual(exc.code, 'not_price_formatted')


	def test_price_with_correct_integer(self):
		self.assertEquals(None, v.price(1246.78))
		self.assertEquals(None, v.price(1245.34))
		self.assertEquals(None, v.price(12431))		


	def test_price_with_incorrect_integer(self):
		# self.assertRaisesMessage(ValidationError,_('Not a valid price. 2 decimals maximum and numbers only is allowed.'),v.price, 12345.78978)
		with self.assertRaises(ValidationError) as e:
			v.price(12345.78978)
		exc  = e.exception
		self.assertEqual(exc.code, 'not_price_formatted')


	def test_price_with_numeric_string_three_decimals(self):
		# self.assertRaisesMessage(ValidationError,_('Not a valid price. 2 decimals maximum and numbers only is allowed.'),v.price, '1234.567')
		with self.assertRaises(ValidationError) as e:
			v.price('1234.567')
		exc  = e.exception
		self.assertEqual(exc.code, 'not_price_formatted')


	def test_price_with_object(self):
		# self.assertRaisesMessage(ValidationError,_('Not a valid price. 2 decimals maximum and numbers only is allowed.'), v.price, object)
		with self.assertRaises(ValidationError) as e:
			v.price(object)
		exc  = e.exception
		self.assertEqual(exc.code, 'not_price_formatted')

	# =======================================================================================
	# PRICE_TOO_HIGH VALIDATOR
	# =======================================================================================
	def test_price_too_high_with_correct_price_many_decimals(self):
		self.assertEquals(None, v.price_too_high(1246.783894734903479387))


	def test_price_too_high_with_string__correct_price_many_decimals(self):
		self.assertEquals(None, v.price_too_high('1246.7811111111111111'))
		

	def test_price_too_high_with_object(self):
		# self.assertRaisesMessage(ValidationError,_('This price seems too high. Please make sure it is correct.'), v.price_too_high, object)
		with self.assertRaises(ValidationError) as e:
			v.price_too_high(object)
		exc  = e.exception
		self.assertEqual(exc.code, 'price_too_high')


	def test_price_too_high_with_mix_with_letters(self):
		# self.assertRaisesMessage(ValidationError,_('This price seems too high. Please make sure it is correct.'), v.price_too_high, '123.7a')
		with self.assertRaises(ValidationError) as e:
			v.price_too_high('123.7a')
		exc  = e.exception
		self.assertEqual(exc.code, 'price_too_high')


	def test_price_too_high_with_correct_price(self):
		self.assertEquals(None, v.price_too_high(1246.78))


	def test_price_too_high_with_string__correct_price(self):
		self.assertEquals(None, v.price_too_high('1246.78'))
		

	# =======================================================================================
	# NON_NUMERIC VALIDATOR
	# =======================================================================================
	
	def test_non_numeric_with_string(self):
		self.assertEquals(None, v.non_numeric('jhksdhjkdhdjk'))
		

	def test_non_numeric_with_mix_of_numbers_and_letters(self):
		self.assertRaisesMessage(ValidationError,_('Expression should not contain numeric values'),v.non_numeric,'taa9864867')
		with self.assertRaises(ValidationError) as e:
			v.non_numeric('taa9864867')
		exc  = e.exception
		self.assertEqual(exc.code, 'no_numeric_expected')
		

	def test_non_numeric_with_int(self):
		self.assertRaisesMessage(ValidationError,_('Expression should not contain numeric values'),v.non_numeric,78979879789)
		with self.assertRaises(ValidationError) as e:
			v.non_numeric(78979879789)
		exc  = e.exception
		self.assertEqual(exc.code, 'no_numeric_expected')


	def test_non_numeric_with_obj(self):
		self.assertRaisesMessage(ValidationError,_('Expression should not contain numeric values'),v.non_numeric,object)
		with self.assertRaises(ValidationError) as e:
			v.non_numeric(object)
		exc  = e.exception
		self.assertEqual(exc.code, 'no_numeric_expected')


	def test_non_numeric_with_french_character(self):
		self.assertEquals(None,v.non_numeric(u'àâçÀéÉèêëîïôûùüÿñæœ'))

	# =======================================================================================
	# NUMERIC_ONLY VALIDATOR
	# =======================================================================================

	def test_numeric_only_with_string(self):
		
		self.assertRaisesMessage(ValidationError,_('Expression contains letters'),v.numeric_only,'aakjahak')
		with self.assertRaises(ValidationError) as e:
			v.numeric_only('aakjahak')
		exc  = e.exception
		self.assertEqual(exc.code, 'numeric_only_expected')


	def test_numeric_only_with_obj(self):
		self.assertRaisesMessage(ValidationError,_('Expression contains letters'),v.numeric_only,object)
		with self.assertRaises(ValidationError) as e:
			v.numeric_only(object)

		exc  = e.exception
		self.assertEqual(exc.code, 'numeric_only_expected')

	def test_numeric_only_with_french_character(self):
		self.assertRaisesMessage(ValidationError,_('Expression contains letters'),v.numeric_only,u'àâçÀéÉèêëîïôûùüÿñæœ')
		with self.assertRaises(ValidationError) as e:
			v.numeric_only(u'àâçÀéÉèêëîïôûùüÿñæœ')

		exc  = e.exception
		self.assertEqual(exc.code, 'numeric_only_expected')
