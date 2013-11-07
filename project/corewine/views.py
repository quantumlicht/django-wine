import logging

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from django.core.exceptions import ObjectDoesNotExist

from django.forms.models import inlineformset_factory
from django.forms.models import modelform_factory

from django.views.i18n import set_language
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic import DetailView, CreateView, UpdateView
from braces.views import LoginRequiredMixin

from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext

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

    return render(request, 'corewine/index.html')


class WineActionMixin(object):

    @property
    def action(self):
        msg = "{0} is missing action.".format(self.__class__)
        raise NotImplementedError(msg)

    def form_valid(self, form):
        msg = "Wine {0}!".format(self.action)
        messages.success(self.request, msg)
        return super(WineActionMixin, self).form_valid(form)


class WineCreateView(WineActionMixin, LoginRequiredMixin, CreateView):
    model = Wine
    form_class = WineForm
    action = 'created'
        

    # def post(self, *args, **kwargs):
    #     self.request.POST = self.request.POST.copy()  # makes the request mutable

    #     regionForm = modelform_factory(Region, fields=('region',))
    #     appelationForm = modelform_factory(Appelation, fields=('appelation',))
    #     producerForm = modelform_factory(Producer, fields=('producer',))
    #     tagForm = modelform_factory(Tag, fields=('tag',))


    #     form_dict = {
    #         'region': regionForm,
    #         'appelation': appelationForm,
    #         'producer': producerForm,
    #         # 'tag': tagForm
    #     }
    #     for k, modelForm in form_dict.iteritems():
    #         model_class = modelForm.Meta.model
    #         # log.debug('current model_class is: %s' % model_class)
    #         # log.debug('request is %s' % self.request.POST[k])
    #         try:
    #             obj = model_class.objects.get( **{k: self.request.POST[k]} )
    #             # log.debug("object exists. %s pk from post request %s " % (model_class,obj.pk))
    #             self.request.POST[k] = obj.id
    #         except ObjectDoesNotExist as e:
    #             log.error('Exception %s' % e)
    #             return super(WineCreateView,self).post(self.request, *args, **kwargs)
    #             f = modelForm(self.request.POST)            
    #             # log.debug('errors %s' % f.errors)
    #             if f.is_valid():
    #                 model_instance = f.save()
    #                 self.request.POST[k] = model_instance.pk
        
    #     return super(WineCreateView,self).post(self.request, *args, **kwargs)


class WineUpdateView(LoginRequiredMixin, WineActionMixin, UpdateView):
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


# --------------------------------------------------
class WineReadView(ListAPIView):
    model = Wine

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Wine.objects.all()
        name = self.request.QUERY_PARAMS.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__iexact=name)
        return queryset

# --------------------------------------------------
class AppelationReadView(ListAPIView):
    model = Appelation

    def get_queryset(self):
        return Appelation.objects.all().filter(status='a')


# --------------------------------------------------
class CepageReadView(ListAPIView):
    model = Cepage


# --------------------------------------------------
class CountryReadView(ListAPIView):
    model = Country
    def get_queryset(self):
        return Country.objects.all().filter(status='a')

# --------------------------------------------------
class ProducerReadView(ListAPIView):
    model = Producer


# --------------------------------------------------
class RegionReadView(ListAPIView):
    model = Region


# --------------------------------------------------
class TagReadView(ListAPIView):
    model = Tag
	


