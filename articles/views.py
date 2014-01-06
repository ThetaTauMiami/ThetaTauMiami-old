from django.shortcuts import render

from django.http import HttpResponse
from django.template import Context, loader

from django.http import HttpResponse

def index(request):
    t = loader.get_template('article_list.html')
    c = Context({'eventType': 'All'})
    return HttpResponse(t.render(c))
 
def service(request):
    t = loader.get_template('article_list.html')
    c = Context({'eventType': 'Service'})
    return HttpResponse(t.render(c))

def professional_development(request):
    t = loader.get_template('article_list.html')
    c = Context({'eventType': 'Professional Development'})
    return HttpResponse(t.render(c))

def social(request):
    t = loader.get_template('article_list.html')
    c = Context({'eventType': 'Social'})
    return HttpResponse(t.render(c))
