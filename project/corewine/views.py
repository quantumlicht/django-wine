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

from .forms import WineForm, WineSearchForm

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


# ==============================
# MIXINS
# ==============================
class WineActionMixin(object):

    @property
    def action(self):
        msg = "{0} is missing action.".format(self.__class__)
        raise NotImplementedError(msg)

    def form_valid(self, form):
        msg = "Wine {0}!".format(self.action)
        messages.success(self.request, msg)
        return super(WineActionMixin, self).form_valid(form)


class WineSearchMixin(object):

    def get_queryset(self):
        ALLOWED_FIELDS  = [ 'wineType','name', 'year', 'code_saq', 'date', 'alcool',\
            'price', 'nose_intensity', 'mouth_intensity', 'persistance', 'rating'
        ]

        ALLOWED_RELATED_FIELDS = ['tag', 'cepage', 'producer', 'region' ,'country',\
            'teint', 'aroma', 'tanin', 'taste'
        ]

        queryset = Wine.objects.prefetch_related()
        field_lookup = self.request.GET.get('look', None)
        query = self.request.GET.get('q', None)

        if not field_lookup or not query:
            return queryset.distinct()
        else:
            if field_lookup in ALLOWED_FIELDS:
                filter = field_lookup + '__icontains'
                queryset = queryset.filter(**{filter: query})
            elif field_lookup in ALLOWED_RELATED_FIELDS:
                filter = field_lookup+'__'+field_lookup+'__icontains'
                queryset = queryset.filter(**{filter: query})

            return queryset.distinct()
# ==============================
# VIEWS
# ==============================

def index(request):
    top = Wine.objects.all().order_by('rating').reverse()[:5]
    return render(request, 'corewine/index.html', {'top':top})


class WineSearchView(FormView):
    template_name = 'corewine/wine_search.html'
    form_class = WineSearchForm
    http_method_names = ['get']
    

class WineCreateView(WineActionMixin, LoginRequiredMixin, CreateView):
    model = Wine
    form_class = WineForm
    action = 'created'
        

class WineUpdateView(LoginRequiredMixin, WineActionMixin, UpdateView):
    model = Wine
    form_class = WineForm
    action = 'updated'


class WineListView(WineSearchMixin, ListView):
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
class WineReadView(WineSearchMixin, ListAPIView):
    model = Wine
    
# --------------------------------------------------
class AppelationReadView(ListAPIView):
    model = Appelation
    def get_queryset(self):
        queryset = Appelation.approved.all()
        country = self.request.QUERY_PARAMS.get('country',None)
        if country is not None:
            queryset = queryset.filter(country__id=country)

        return queryset


# --------------------------------------------------
class CepageReadView(ListAPIView):
    model = Cepage
    def get_queryset(self):
        queryset = Cepage.approved.all()
        cepage = self.request.QUERY_PARAMS.get('cepage', None)
        color = self.request.QUERY_PARAMS.get('type', None)
        if color=='':
            color = None
        if cepage=='':
            cepage = None
            
        if cepage is not None:
            queryset = queryset.filter(cepage__icontains=cepage)

        if color is not None:
            queryset = queryset.filter(wineType__iexact=color)

        return queryset 

# --------------------------------------------------
class CountryReadView(ListAPIView):
    model = Country
    queryset = Country.approved.all()

# --------------------------------------------------
class ProducerReadView(ListAPIView):
    model = Producer
    def get_queryset(self):
        queryset = Producer.approved.all()
        country = self.request.QUERY_PARAMS.get('country',None)
        if country is not None:
            queryset = queryset.filter(country__id=country)

        return queryset

# --------------------------------------------------
class RegionReadView(ListAPIView):
    model = Region

    def get_queryset(self):
        queryset = Region.approved.all()
        country = self.request.QUERY_PARAMS.get('country',None)
        if country is not None:
            queryset = queryset.filter(country__id=country)

        return queryset

# --------------------------------------------------
class TagReadView(ListAPIView):
    model = Tag
    def get_queryset(self):
        queryset = Tag.approved.all()
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


