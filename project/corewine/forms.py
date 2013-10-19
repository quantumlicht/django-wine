import json
from django.forms import ModelForm, ValidationError
from .models import Wine


class WineForm(ModelForm):

    class Meta:
        model = Wine
    
    def clean(self):
        
        cleaned_data = super(WineForm, self).clean()

        if cleaned_data.get('wineType')=='Red':
            raise ValidationError('Red wines need to have tanin described.')

        return cleaned_data
    # fieldsets = list(WineAdmin.fieldsets)
    # field_list = Wine._meta.fields + Wine._meta.many_to_many

    # EXCLUDED_FIELDS_LIST = ['rating']

    # # prepare field metadata
    # fields_data = {}
    # for item in field_list:
    #     fields_data[item.attname] = {"type": item.get_internal_type(), "verbose": item.verbose_name}
    

    # # parse WineAdmin fieldsets structure to extract the list of fields for each fieldset and link the metadata to it.
    # # WARNING: it currently does not support having tuples as fields items. In other words, there should only be 3 nested levels to the fieldsets tuple.
    # json_dict = {}
    # for fieldset in list(fieldsets):
    #     fieldset_name = fieldset[0]
    #     fieldset_fields = list(fieldset[1]['fields'])
        
    #     tmp_dict = {}
    #     for item in fieldset_fields:
    #         if item in fields_data.keys() and not item in EXCLUDED_FIELDS_LIST:
    #             tmp_dict[item] = fields_data[item]
                        
    #     json_dict[fieldset_name] = tmp_dict

    # remove empty keys
    # json_dict = dict((k, v) for k, v in json_dict.iteritems() if v)        

    # prepare as json to be use by javascript in the page
    # fields_data = json.dumps(json_dict)
    
    # this field will contain all the fields we want to show, as well as useful metadata
    # hidden_field = CharField(max_length=64, widget=HiddenInput(attrs={'data':fields_data}))
    