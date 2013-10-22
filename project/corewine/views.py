from django.shortcuts import render
from django.forms.models import model_to_dict
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic import DetailView


from .forms import WineForm
from .models import Wine, Cepage, Teint, Tag

from rest_framework.generics import (
	ListAPIView
)


def index(request):
    return render(request, 'corewine/index.html')


class TastingView(FormView):
    template_name = 'corewine/tasting.html'
    form_class = WineForm
    success_url = '/wine'

    def form_valid(self, form):
        form.save()
        return super(TastingView, self).form_valid(form)


class WineListView(ListView):
    model = Wine
    context_object_name = 'wine_list'


class WineDetailView(DetailView):
    model = Wine
    template_name = 'corewine/wine_detail.html'
    context_object_name = 'wine'
    

    def get_context_data(self, **kwargs):
        context = super(WineDetailView, self).get_context_data(**kwargs)
        context['arr_cepage'] = Wine.arr_cepage(self.get_object())
        context['arr_tag'] = Wine.arr_tag(self.get_object())
        return context



# ===================================
# API VIEWS
# ===================================

# READ ONLY 
class CepageReadView(ListAPIView):
	model = Cepage


class TagReadView(ListAPIView):
	model = Tag


class TeintReadView(ListAPIView):
	model = Teint

# WRITE


	


