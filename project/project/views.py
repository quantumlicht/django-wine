import logging
from django.shortcuts import render

log = logging.getLogger(__name__) 

def landing(request):
	log.debug('test')
	return render(request,'landing.html')