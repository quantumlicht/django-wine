import logging
from core.validators import non_numeric,validate_future_date
from django.core.exceptions import ObjectDoesNotExist
from django.forms import (
    ModelForm,
    ValidationError,
    CharField,
    TextInput,
    RadioSelect,
    MultipleChoiceField,
    DateField
)
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, Div
from crispy_forms.bootstrap import FormActions, AppendedText, InlineRadios, TabHolder, Tab

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


# Check this snippet
# https://docs.djangoproject.com/en/dev/howto/custom-model-fields/#writing-custom-model-fieldsv
# class HandField(CharField):

#     description = "A hand of cards (bridge style)"

#     def __init__(self, *args, **kwargs):
#         kwargs['max_length'] = 104
#         super(HandField, self).__init__(*args, **kwargs)

class RegionTypeAheadField(CharField):
    # Override __init__ method to pass additional arguments if we cannot find a good way to retrieve the model field linked to this form field.
    default_validators = [non_numeric]

    def clean(self, value):
        value = super(RegionTypeAheadField, self).clean(value)
        # log.debug('value %s' % value)
        # errors = non_numeric(value)
        try:
            # log.debug('errors %s' % errors)
            obj = Region.objects.get(region=value)    
            return obj
        except ObjectDoesNotExist as e:
            reg = Region(region=value,status='p')
                
            return reg


class AppelationTypeAheadField(CharField):
    # Override __init__ method to pass additional arguments if we cannot find a good way to retrieve the model field linked to this form field.
    default_validators = [non_numeric]

    def clean(self, value):
        value = super(AppelationTypeAheadField, self).clean(value)
        # log.debug('value %s' % value)
        # errors = non_numeric(value)
        try:
            # log.debug('errors %s' % errors)
            obj = Appelation.objects.get(appelation=value)    
            return obj
        except ObjectDoesNotExist as e:
            reg = Appelation(appelation=value,status='p')
                
            return reg


class ProducerTypeAheadField(CharField):
    # Override __init__ method to pass additional arguments if we cannot find a good way to retrieve the model field linked to this form field.
    default_validators = [non_numeric]

    def clean(self, value):
        value = super(ProducerTypeAheadField, self).clean(value)
        # log.debug('value %s' % value)
        # errors = non_numeric(value)
        try:
            # log.debug('errors %s' % errors)
            obj = Producer.objects.get(producer=value)    
            return obj
        except ObjectDoesNotExist as e:
            reg = Producer(producer=value,status='p')
                
            return reg


class CountryTypeAheadField(CharField):
    # Override __init__ method to pass additional arguments if we cannot find a good way to retrieve the model field linked to this form field.
    default_validators = [non_numeric]

    def clean(self, value):
        value = super(CountryTypeAheadField, self).clean(value)
        # log.debug('value %s' % value)
        # errors = non_numeric(value)
            # log.debug('errors %s' % errors)
        try:
            obj = Country.objects.get(country=value)    
            return obj
        except ObjectDoesNotExist as e:
            msg = 'Invalid Country'
            raise ValidationError(msg)
                

# class multiselectfield(MultipleChoiceField):
#     def clean(self, value):
#         value = super(multiselectfield,self).clean(value)
#         log.debug('value %s' % value)
#         return value


class WineForm(ModelForm):

    region = RegionTypeAheadField()
    country = CountryTypeAheadField()
    producer = ProducerTypeAheadField()
    appelation = AppelationTypeAheadField()

    class Meta:
        model = Wine
        fields = (
            'wineType','name','region', 'producer','year','country','alcool','appelation',\
            'date', 'code_saq', 'price', 'mouth_intensity', 'nose_intensity',\
            'rating', 'teint', 'aroma', 'taste', 'acidity', 'tanin', 'persistance', 'cepage', 'tag'
        )

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

    def clean_cepage(self):
        data = self.cleaned_data['cepage']
        log.debug('cepage %s' % data)
        return data

    def clean_date(self):
        data = self.cleaned_data['date']
        validate_future_date(data)
        return data    

# class WineForm(ModelForm):

#     class Meta: 
#         model = Wine

    # def __init__(self,*args,**kwargs):
    #     super(WineForm,self).__init__(*args,**kwargs)
    #     self.helper = FormHelper()
    #     self.form_id = 'wine_form'
    #     self.label_class= 'col-lg-12'
    #     self.field_class= 'col-lg-12'
    #     self.form_method = 'post'
    #     self.form_class = 'form_horizontal'
    #     self.form_action = reverse('corewine:tasting')

    #     self.helper.add_input(Submit('submit', _('Submit')))

    #     self.helper.layout = Layout(
    #         InlineRadios('wineType'),
    #         Div(Field('name'), css_class='col-lg-4'),
    #         Div(Field('producer'), css_class='col-lg-4'),
    #         Div(Field('year'), css_class='col-lg-4'),
    #         Div(Field('appelation'),css_class='col-lg-4'),
    #         'region',
    #         'country',
    #         'cepage',
    #         Div(AppendedText('alcool', '%'),css_class="col-lg-4"),
    #         Div('date', css_class='col-lg-4'),
    #         Div('code_saq', css_class='col-lg-4'),
    #         Div(AppendedText('price', '$'),css_class='col-lg-4'),
    #         Div('nose_intensity',css_class='col-lg-4'),
    #         Div('aroma',css_class='col-lg-4'),
    #         Div('mouth_intensity',css_class='col-lg-4'),
    #         Div('persistance',css_class='col-lg-4'),
    #         Div('taste',css_class='col-lg-4'),
    #         Div('acidity',css_class='col-lg-4'),
    #         Div('tanin',css_class='col-lg-4'),
    #         'Tags',
    #         'tag',
    #         'rating',
    #         FormActions('Sign in', css_class='btn-primary')
    #     )
