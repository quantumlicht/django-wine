from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	
	return render(request, 'index.html')


def publish_tasting(request):
    return HttpResponse("You are publishing a tasting")
