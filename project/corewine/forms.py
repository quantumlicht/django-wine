import logging, re

from core.validators import non_numeric, validate_future_date
from django.core.exceptions import ObjectDoesNotExist
from django.forms import (
    ModelForm,
    ValidationError,
    CharField,
    TextInput,
    RadioSelect,
    Select,
    MultipleChoiceField,
    ChoiceField,
    DateField
)
from django.forms.widgets import SelectMultiple
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, Div
from crispy_forms.bootstrap import FormActions, AppendedText, InlineRadios, TabHolder, Tab
from django.db import models
from .models import (
    Wine,
    Region,
    Appelation,
    Producer,
    Country,
    Tag,
    Cepage,
)
log = logging.getLogger(__name__)
        
WINE_TYPES = (
    ('w', _('White')),
    ('r', _('Red'))
)

class RegionTypeAheadField(ChoiceField):
    # Override __init__ method to pass additional arguments if we cannot find a good way to retrieve the model field linked to this form field.
    default_validators = [non_numeric]

    def clean(self, value):
        # errors = non_numeric(value)
        try:
            # log.debug('errors %s' % errors)
            obj = Region.objects.get(region=value)    
        except ObjectDoesNotExist as e:
            obj = Region(region=value,status='p')
                
        self.choices.append((obj, value))
        # log.debug('Region::clean choices %s' % self.choices)
        value = super(RegionTypeAheadField, self).clean(value)
        return obj


class AppelationTypeAheadField(ChoiceField):
    # Override __init__ method to pass additional arguments if we cannot find a good way to retrieve the model field linked to this form field.
    default_validators = [non_numeric]

    def clean(self, value):
        # errors = non_numeric(value)
        try:
            # log.debug('errors %s' % errors)
            obj = Appelation.objects.get(appelation=value)    
        except ObjectDoesNotExist as e:
            obj = Appelation(appelation=value,status='p')
                
        self.choices.append((obj, value))
        # log.debug('Appelation::clean choices %s' % self.choices)
        value = super(AppelationTypeAheadField, self).clean(value)
        return obj


class ProducerTypeAheadField(ChoiceField):
    # Override __init__ method to pass additional arguments if we cannot find a good way to retrieve the model field linked to this form field.
    default_validators = [non_numeric]

    def clean(self, value):
        # errors = non_numeric(value)
        try:
            # log.debug('errors %s' % errors)
            obj = Producer.objects.get(producer=value)    
        except ObjectDoesNotExist as e:
            obj = Producer(producer=value,status='p')
                    
        self.choices.append((obj, value))
        # log.debug('Producer::clean choices %s' % self.choices)
        value = super(ProducerTypeAheadField, self).clean(value)
        return obj


class TagField(MultipleChoiceField):
    __metaclass__ = models.SubfieldBase
    
    def to_python(self, value):
        arr = []
        for tag in value:
            try:
                obj = Tag.objects.get(tag=tag)
                arr.append(obj.id)
            except ObjectDoesNotExist as e:
                non_numeric(tag)
                obj = Tag(tag=tag,status='p')            
                obj.save()
                self.choices.append((value,tag))
                arr.append(obj.id)
        log.debug('to_python::arr %s' % arr)
        return arr


    def validate(self, value):
        # super(TagField, self).validate(value)
        log.debug('validate::value %s' %  value)
        return value
        for tag in value:
            non_numeric(tag)


class CepageField(MultipleChoiceField):
    __metaclass__ = models.SubfieldBase
    
    def to_python(self, value):
        arr = []
        for cepage in value:
            try:
                obj = Cepage.objects.get(cepage=cepage)
                arr.append(obj)
            except ObjectDoesNotExist as e:
                non_numeric(cepage)
                obj = Cepage(cepage=cepage,status='p')            
                obj.save()
                self.choices.append((value,cepage))
                arr.append(obj)
        log.debug('to_python::arr %s' % arr)
        return arr


    def validate(self, value):
        # super(TagField, self).validate(value)
        log.debug('validate::value %s' %  value)
        return value
        for cepage in value:
            non_numeric(cepage)


class WineForm(ModelForm):

    region = RegionTypeAheadField()
    # country = CountryTypeAheadField()
    producer = ProducerTypeAheadField()
    appelation = AppelationTypeAheadField()
    tag = TagField()
    cepage = CepageField()

    
    class Meta:
        model = Wine
        fields = (
            'wineType','name', 'producer', 'country', 'region', 'cepage', 'year', 'alcool', 'appelation',\
            'date', 'code_saq', 'price', 'mouth_intensity', 'nose_intensity',\
            'rating', 'teint', 'aroma', 'taste', 'acidity', 'tanin', 'persistance', 'tag'
        )

        widgets = {
            'wineType': RadioSelect
        }


    def clean_appelation(self):
        data  = self.cleaned_data['appelation']
        data.status='p'
        data.save()
        return data

    def clean_region(self):
        data  = self.cleaned_data['region']
        data.status='p'
        data.save()
        return data

    def clean_producer(self):
        data  = self.cleaned_data['producer']
        data.status='p'
        data.save()
        return data

    def clean_code_saq(self):
        data = self.cleaned_data['code_saq']
        data = re.sub(r"[\s\.\-\,]", '', data)
        return data


    def clean_cepage(self):
        arr = []
        data = self.cleaned_data['cepage']
        winetype = self.cleaned_data['wineType']
        for cepage in data:
            log.debug('cepage before %s' % cepage)
            cepage.wineType = winetype
            cepage.save()
            log.debug('cepage after %s' % cepage)
            arr.append(cepage.id)

        log.debug('cleaned_cepage %s' % data)
        # for cepage in data:
        #     cepage.save()

        return data

    def clean_date(self):
        data = self.cleaned_data['date']
        validate_future_date(data)
        return data    


    # def clean(self):
    #     wineType = self.cleaned_data['wineType']
        # cepages = self.cleaned_data['cepage']
        # log.debug('form_clean:: cepage %s , wineType %s ' % (cepages,wineType))

    # def save(self, commit=True):
    #     log.debug('clean_data %s' % self.cleaned_data)
    #     instance = super(WineForm, self).save(commit=False)

    #     return instance

    def clean_tag(self):
        data = self.cleaned_data['tag']
        log.debug('cleaned_data %s' % data)
        # for tag in data:
        #     tag.save()
        return data

    def __init__(self,*args,**kwargs):
        super(WineForm, self).__init__(*args,**kwargs)
        self.fields['wineType'].choices = WINE_TYPES
        self.fields['region'].choices  =  [(x,x.region) for x in Region.approved.all()]
        self.fields['producer'].choices = [(x,x.producer) for x in Producer.approved.all()]
        self.fields['appelation'].choices = [(x,x.appelation) for x in Appelation.approved.all()]
        # self.fields['tag'].choices = [(x,x.tag) for x in Tag.approved.all()]
        self.fields['cepage'].choices = [(x,x.cepage) for x in Cepage.approved.all()]

        self.helper = FormHelper()
        self.form_id = 'wine_form'
        self.label_class= 'col-lg-12'
        self.field_class= 'col-lg-12'
        self.form_method = 'post'
        self.form_class = 'form_horizontal'
        self.form_action = reverse('corewine:tasting')

        self.helper.add_input(Submit('submit', _('Submit')))

        self.helper.layout = Layout(
            Fieldset(_('Type'),
                InlineRadios('wineType'),
            ),
            Fieldset(_('General Information'),
                Div(Field('name'), css_class='col-lg-3'),
                Div(Field('producer'), css_class='col-lg-3'),
                Div(Field('year'), css_class='col-lg-3'),
                Div('date', css_class='col-lg-3'),
                Div(AppendedText('alcool', '%'),css_class="col-lg-3"),
                Div('code_saq', css_class='col-lg-3'),
                Div('cepage',css_class='col-lg-3'),
                Div(AppendedText('price', '$'),css_class='col-lg-3'),
            ),
            Fieldset(_('Geography'),
                Div(Field('appelation'),css_class='col-lg-3'),
                Div(Field('region'),css_class='col-lg-3'),
                Div(Field('country'),css_class='col-lg-3'),
            ),
            Fieldset(_('Eye'),
                Div(Field('teint'), css_class='col-lg-2'),
                Div('aroma',css_class='col-lg-2'),
            ),
            Fieldset(_('Nose'),
                Div('nose_intensity',css_class='col-lg-2'),
            ),
            Fieldset(_('Mouth'),
                Div('mouth_intensity',css_class='col-lg-2'),
                Div('persistance',css_class='col-lg-2'),
                Div('taste',css_class='col-lg-2'),
                Div('tanin',css_class='col-lg-2'),
                Div('acidity',css_class='col-lg-2'),
            ),
            Fieldset(_('Extra information'),
                Div('tag',css_class='col-lg-4'),
                Div('rating',css_class='col-lg-4'),
            ),
            FormActions('Sign in', css_class='btn-primary')
        )
