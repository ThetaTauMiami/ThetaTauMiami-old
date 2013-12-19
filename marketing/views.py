from django.shortcuts import render
from django.template import Context, loader

from django.http import HttpResponse

# Create your views here.
def index(request):
    t = loader.get_template('index.html')
    c = Context({})
    return HttpResponse(t.render(c))