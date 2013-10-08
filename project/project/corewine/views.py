from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the home page of wine")


def home(request):
    return HttpResponse("Hello, world. You're at the home page")


def publish_tasting(request):
    return HttpResponse("You are publishing a tasting")
