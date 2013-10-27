from django.shortcuts import render
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic import DetailView, CreateView, UpdateView
from braces.views import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _
import logging

log = logging.getLogger(__name__) 

from .forms import WineForm
from .models import (
    Wine,
    Cepage,
    Teint,
    Tag,
    Region,
    Appelation,
    Producer,
    Country
)

from rest_framework.generics import (
	ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)


def index(request):
    log.debug('test')
    return render(request, 'corewine/index.html')


class WineActionMixin(object):

    @property
    def action(self):
        msg = "{0} is missing action.".format(self.__class__)
        raise NotImplementedError(msg)

    def form_valid(self, form):
        msg = "Wine {0}!".format(self.action)
        messages.success(self.request, 'test Message')
        return super(WineActionMixin, self).form_valid(form)


class WineCreateView(WineActionMixin, CreateView):
    model = Wine
    form_class = WineForm
    action = 'Creation!'


class WineUpdateView(WineActionMixin, UpdateView):
    model = Wine
    form_class = WineForm
    action = 'updated'


class WineListView(ListView):
    model = Wine
    context_object_name = 'wine_list'


class WineDetailView(DetailView):
    model = Wine
    # template_name = 'corewine/wine_detail.html'
    context_object_name = 'wine'
    
    def get_context_data(self, **kwargs):
        context = super(WineDetailView, self).get_context_data(**kwargs)
        context['arr_cepage'] = Wine.arr_cepage(self.get_object())
        context['arr_tag'] = Wine.arr_tag(self.get_object())
        return context

        
    # template_name = 'corewine/tasting.html'
    # form_class = WineForm
    # success_url = '/wine'

    # def form_valid(self, form):
    #     form.save()
    #     return super(TastingView, self).form_valid(form)


# ===================================
# API VIEWS
# ===================================

# READ ONLY 

# --------------------------------------------------
class TeintReadView(ListAPIView):
    model = Teint


# READ-WRITE

# --------------------------------------------------
class AppelationCreateReadView(ListCreateAPIView):
    model = Appelation


# --------------------------------------------------
class CepageCreateReadView(ListCreateAPIView):
    model = Cepage


# --------------------------------------------------
class CountryCreateReadView(ListCreateAPIView):
    model = Country


# --------------------------------------------------
class ProducerCreateReadView(ListCreateAPIView):
    model = Producer


# --------------------------------------------------
class RegionCreateReadView(ListCreateAPIView):
    model = Region


# --------------------------------------------------
class TagCreateReadView(ListCreateAPIView):
    model = Tag
	


