from django.shortcuts import render

from django.http import HttpResponse
from django.template import Context, loader

from django.http import HttpResponse

from articles.models import Article

def index(request):
    t = loader.get_template('article_list.html')
    article_list = Article.objects.all()
    if len(article_list) == 0:
        article_list = None
    c = Context({'eventType': 'All', 'article_list': article_list})
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
