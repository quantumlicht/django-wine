from django.shortcuts import render
from django.contrib import messages
from django.forms.models import model_to_dict
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic import DetailView, CreateView, UpdateView
from django.utils.translation import ugettext_lazy as _
import logging

log = logging.getLogger(__name__) 

from .forms import WineForm
from .models import Wine, Cepage, Teint, Tag
from braces.views import LoginRequiredMixin

from rest_framework.generics import (
	ListAPIView
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
        message.info(self.request, msg)
        return super(WineActionMixin, self).form_valid(form)


class WineCreateView(LoginRequiredMixin, WineActionMixin, CreateView):
    model = Wine
    action = _('created')


class WineUpdateView(LoginRequiredMixin, WineActionMixin, UpdateView):
    model = Wine
    action = _('updated')


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
class CepageReadView(ListAPIView):
	model = Cepage


class TagReadView(ListAPIView):
	model = Tag


class TeintReadView(ListAPIView):
	model = Teint

# WRITE


	


