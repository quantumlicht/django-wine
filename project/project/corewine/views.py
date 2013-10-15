from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from project.corewine.forms import WineForm
from project.corewine.models import Wine
from django.views.generic.edit import FormView


def index(request):
    return render(request, 'corewine/index.html')


class TastingView(FormView):
    template_name = 'corewine/tasting.html'
    form_class = WineForm
    success_url = '/wine'

    def form_valid(self, form):
        form.save()
        return super(TastingView, self).form_valid(form)
