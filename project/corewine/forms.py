import json
from django.forms import (
    ModelForm,
    ValidationError,
    CharField,
    TextInput,
    Textarea,
    RadioSelect
)
from .models import Wine


class WineForm(ModelForm):

    class Meta:
        model = Wine

        fields = (
            'wineType', 'name','producer','year','appelation','country','region','alcool',\
            'date', 'code_saq', 'price', 'mouth_intensity', 'nose_intensity',\
            'rating', 'teint', 'aroma', 'taste', 'acidity', 'tanin', 'persistance', 'cepage', 'tag'
        )
        widgets = {
            'region': TextInput(),
            'appelation': TextInput(),
            'country': TextInput(),
            'producer': TextInput(),
            'wineType': RadioSelect(),
            'cepage' : TextInput(),
            'tag': TextInput(),
        }

    # def clean_tanin(self):
    #     # cleaned_data = super(WineForm, self).clean()
    #     winetype = self.cleaned_data['wineType']
    #     tanin = self.cleaned_data['tanin']
    #     if winetype == 'White':
    #         tanin = ''
    #         # raise ValidationError('Red wines need to have tanin described.')
    #     return tanin
    #     # return cleaned_data
    

    
    