from django.shortcuts import render
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic import DetailView, CreateView, UpdateView
from braces.views import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _
import logging


from .forms import WineForm
from .models import (
    Wine,
    Cepage,
    Teint,
    Tag,
    Region,
    Appelation,
    Producer,
    Country,
)

from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

log = logging.getLogger(__name__) 


def index(request):
    log.debug('Index page')
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

    def post(self, *args, **kwargs):
        self.request.POST = self.request.POST.copy()  # makes the request mutable

        regionForm = modelform_factory(Region, fields=('region',))
        appelationForm = modelform_factory(Appelation, fields=('appelation',))
        producerForm = modelform_factory(Producer, fields=('producer',))

        form_dict = {
            'region': regionForm,
            'appelation': appelationForm,
            'producer': producerForm
        }
        for k, modelForm in form_dict.iteritems():
            model_class = modelForm.Meta.model
            log.debug('current model_class is: %s' % model_class)
            log.debug('request is %s' % self.request.POST[k])
            try:
                obj = model_class.objects.get( **{k: self.request.POST[k]} )
                log.debug("object exists. %s pk from post request %s " % (model_class,obj.pk))
                self.request.POST[k] = obj.id
            except ObjectDoesNotExist as e:
                log.error('Exception %s' % e)
                f = modelForm(self.request.POST)            
                log.debug('errors %s' % f.errors)
                if f.is_valid():
                    model_instance = f.save()
                    self.request.POST[k] = model_instance.pk
        
        return super(WineCreateView,self).post(self.request, *args, **kwargs)


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
	


