from django.forms import ModelForm, Textarea, SelectMultiple, DateInput, TextInput, Select,RadioSelect, Form, CharField, URLField, DateField, extras
from project.corewine.models import Wine
from django.contrib.admin.widgets import AdminDateWidget

class WineForm(ModelForm):
    class Meta:
        model = Wine
        widgets = {}

        field_list = Wine._meta.fields + Wine._meta.many_to_many


        def getWidgetType(field):
            fieldtype = field.get_internal_type()
            if  fieldtype == 'ManyToManyField':
                return SelectMultiple(attrs={'class': 'form-control'})

            elif field == 'DateField':
                return extras.SelectDateWidget
            
            elif fieldtype == 'CharField':
                return TextInput(attrs={'class': 'form-control'})

            elif fieldtype in ['IntegerField', 'FloatField', 'DecimalField']:
                if field.choices:
                    return Select(attrs={'class': 'form-control'})
                else:
                    return TextInput(attrs={'class': 'form-control'})
            
            elif fieldtype == 'ForeignKey':    
                return RadioSelect(attrs={'class': 'form-control'}, choices=field.choices)

                
        for field in field_list:
            widgets[field.attname] = getWidgetType(field)
