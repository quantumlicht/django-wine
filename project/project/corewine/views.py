from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from project.corewine.forms import WineForm



def index(request):
	return render(request, 'corewine/index.html')


def tasting(request):
    # template_name = 'tasting.html'
    wine_form = WineForm
    # success_url = '/thanks/'

    return render_to_response('corewine/tasting.html', {'wine_form' : wine_form})

   


