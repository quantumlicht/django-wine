from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request, 'corewine/index.html')


def tasting(request):
    return render(request, 'corewine/tasting.html')
