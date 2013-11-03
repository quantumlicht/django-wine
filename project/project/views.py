import logging
from django.shortcuts import render
from django.utils import translation
from django.http import HttpResponseRedirect
log = logging.getLogger(__name__) 

def landing(request):
	log.debug('test')
	return render(request,'landing.html')


def set_language(request):
    next = request.REQUEST.get('next', None)
    if not next:
        next = request.META.get('HTTP_REFERER', None)
    if not next:
        next = '/'
    response = HttpResponseRedirect(next)
    if request.method == 'GET':
        lang_code = request.GET.get('language', None)
        if lang_code and check_for_language(lang_code):
            if hasattr(request, 'session'):
                request.session['django_language'] = lang_code
            else:
                response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
            translation.activate(lang_code)
    return response


def set_lang(request):
	log.debug('test')
	return render(request,'set_lang.html')