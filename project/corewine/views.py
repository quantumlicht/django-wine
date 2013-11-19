import logging

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from django.core.exceptions import ObjectDoesNotExist

from django.forms.models import modelform_factory

from django.views.i18n import set_language
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic import DetailView, CreateView, UpdateView
from braces.views import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

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

from rest_framework.generics import ListAPIView

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
    def get_queryset(self):
        log.debug(self.request.QUERY_PARAMS.get('type', None))
        queryset = Teint.objects.all()
        name = self.request.QUERY_PARAMS.get('type', None)
        if name is not None:
            queryset = queryset.filter(wineType__iexact=name)
        return queryset

# --------------------------------------------------
class WineReadView(ListAPIView):
    model = Wine

    def get_queryset(self):
        queryset = Wine.objects.all()
        name = self.request.QUERY_PARAMS.get('name', None)
        code_saq = self.request.QUERY_PARAMS.get('code', None)
        if name is not None:
            queryset = queryset.filter(name__iexact=name)

        if code_saq is not None:
            queryset = queryset.filter(code_saq__iexact=code_saq)

        return queryset

# --------------------------------------------------
class AppelationReadView(ListAPIView):
    model = Appelation
    queryset = Appelation.approved.all()


# --------------------------------------------------
class CepageReadView(ListAPIView):
    model = Cepage
    queryset = Cepage.approved.all()

# --------------------------------------------------
class CountryReadView(ListAPIView):
    model = Country
    queryset = Country.approved.all()

# --------------------------------------------------
class ProducerReadView(ListAPIView):
    model = Producer
    queryset = Producer.approved.all()

# --------------------------------------------------
class RegionReadView(ListAPIView):
    model = Region
    queryset = Region.approved.all()

# --------------------------------------------------
class TagReadView(ListAPIView):
    model = Tag
    def get_queryset(self):
        queryset = Tag.objects.all()
        tag = self.request.QUERY_PARAMS.get('tag', None)
        color = self.request.QUERY_PARAMS.get('type', None)
        if color=='':
            color = None
        if tag=='':
            tag = None
            
        if tag is not None:
            queryset = queryset.filter(tag__icontains=tag)

        if color is not None:
            queryset = queryset.filter(wineType__iexact=color)

        return queryset 


