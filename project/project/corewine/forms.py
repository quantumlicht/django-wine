from django.forms import ModelForm, Textarea, SelectMultiple, DateInput, TextInput, Select,RadioSelect, Form, CharField, URLField, DateField, extras
from django.forms import HiddenInput
from project.corewine.models import Wine
from project.corewine.admin import WineAdmin
from django.contrib.admin.widgets import AdminDateWidget
import json

def listit(t):
    dictlist = []
    for elem in list(t):
        if isinstance(elem, list):
            return listit(elem)
        elif(isinstance(elem, tuple)):
            return listit(elem)
        else:
            return listit(elem)
        # elif(isinstance(elem, dict)):
        #     for key, value in elem.iteritems():
        #         temp = [key,list(value)]
        #         dictlist.append(temp)
        #     return dictlist   
    # return list(map(listit, t)) if isinstance(t, (list, tuple)) else t

class WineForm(ModelForm):
    fieldset = WineAdmin.fieldsets


    # field_data = str(listit(WineAdmin.fieldsets))

    field_list = Wine._meta.fields + Wine._meta.many_to_many
    field_data = json.dumps([{"name":x.attname, "type": x.get_internal_type(), "verbose": x.verbose_name } for x in field_list])
    hidden_field = CharField(max_length=64, widget=HiddenInput(attrs={'data':field_data}))
    
    class Meta:
        model = Wine
        # widgets = {}
        # fields= '__all__'

        # def getWidgetType(field):
        #     fieldtype = field.get_internal_type()
        #     if  fieldtype == 'ManyToManyField':
        #         return SelectMultiple(attrs={'class': 'form-control'})

        #     elif field == 'DateField':
        #         return extras.SelectDateWidget
            
        #     elif fieldtype == 'CharField':
        #         return TextInput(attrs={'class': 'form-control'})

        #     elif fieldtype in ['IntegerField', 'FloatField', 'DecimalField']:
        #         if field.choices:
        #             return Select(attrs={'class': 'form-control'})
        #         else:
        #             return TextInput(attrs={'class': 'form-control'})
            
        #     elif fieldtype == 'ForeignKey':    
        #         return RadioSelect(attrs={'class': 'form-control'}, choices=field.choices)

                
        # for field in field_list:
        #     widgets[field.attname] = getWidgetType(field)

