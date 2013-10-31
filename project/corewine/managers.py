from django.db import models

class ApprovedManager(models.Manager):
	def get_query_set(self):
		return super(ApprovedManager,self).get_query_set().filter(status='a')

