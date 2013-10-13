from django.forms import ModelForm
from project.corewine.models import Wine


class WineForm(ModelForm):
	class Meta:
		model = Wine

