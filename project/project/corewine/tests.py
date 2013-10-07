"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from project.corewine.models import *


class TagTester(TestCase):

    #===============================================
    # Tag statuses
    def test_is_approved_with_pending(self):
        pending_tag = Tag(wineType='White', tag='gros menseng', status='Pending')
        self.assertEqual(pending_tag.is_approved(), False)

    def test_is_approved_with_approved(self):
        approved_tag = Tag(wineType='White', tag='gros menseng', status='Approved')
        self.assertEqual(approved_tag.is_approved(), True)

    def test_is_approved_with_rejected(self):
        rejected_tag = Tag(wineType='White', tag='gros menseng', status='Rejected')
        self.assertEqual(rejected_tag.is_approved(), False)
    # def test_invalid_wineType(self):
    #     pending_tag = Tag(wineType='White', tag='gros menseng', status='Approved')
    #     pending_tag.save()
    #     self.assertEqual(pending_tag.wineType, 'White')

