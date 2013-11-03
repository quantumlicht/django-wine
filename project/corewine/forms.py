
from django.forms import (
    ModelForm,
    ValidationError,
    CharField,
    TextInput,
    Textarea,
    RadioSelect
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
# class WineForm(ModelForm):

#     class Meta:
#         model = Wine

#         fields = (
#             'wineType','name', 'region','producer','year','country','alcool','appelation',\
#             'date', 'code_saq', 'price', 'mouth_intensity', 'nose_intensity',\
#             'rating', 'teint', 'aroma', 'taste', 'acidity', 'tanin', 'persistance', 'cepage', 'tag'
#         )

    
class WineForm(ModelForm):

    class Meta: 
        model = Wine


    def __init__(self,*args,**kwargs):
        super(WineForm,self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.form_id = 'wine_form'
        self.label_class= 'col-lg-12'
        self.field_class= 'col-lg-12'
        self.form_method = 'post'
        self.form_class = 'form_horizontal'
        self.form_action = reverse('corewine:tasting')

        self.helper.add_input(Submit('submit', _('Submit')))

        self.helper.layout = Layout(
            TabHolder(
                Tab(_('General Info'),
                    Div(Field('name'), css_class='col-lg-4'),
                    'producer',
                    Div(Field('year'), css_class='col-lg-4'),
                    Div('appelation', css_class='col-lg-4'),
                    'region',
                    'country',
                    'cepage',
                    Div(AppendedText('alcool', '%'),css_class="col-lg-4"),
                    Div('date', css_class='col-lg-4'),
                    Div('code_saq', css_class='col-lg-4'),
                    Div(AppendedText('price', '$'),css_class='col-lg-4'),
                ),
                Tab(_('Aromatic profile'),
                    Div('nose_intensity',css_class='col-lg-4'),
                    Div('aroma',css_class='col-lg-4'),
                ),
                Tab(_('Taste profile'),
                    Div('mouth_intensity',css_class='col-lg-4'),
                    Div('persistance',css_class='col-lg-4'),
                    Div('taste',css_class='col-lg-4'),
                    Div('acidity',css_class='col-lg-4'),
                    Div('tanin',css_class='col-lg-4')
                ),
                Tab('Extras',
                    'Tags',
                    'tag',
                    'rating'
                )
            ),

            FormActions('Sign in', css_class='btn-primary')
        )


    region = CharField(widget=TextInput)
    appelation = CharField(widget=TextInput)
    country = CharField(widget=TextInput)
    producer = CharField(widget=TextInput)
    tag = CharField(widget=TextInput)
    #     'country': TextInput(),
    #     'producer': TextInput(),
    #     'wineType': RadioSelect(),
    #     'cepage' : TextInput(),
    # }