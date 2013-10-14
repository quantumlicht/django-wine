from django.forms import ModelForm
from project.corewine.models import Wine


class WineForm(ModelForm):
    class Meta:
        model = Wine

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass