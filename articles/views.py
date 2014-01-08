from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import Context, loader

from articles.models import Article, ArticleEntity

def index(request):
    t = loader.get_template('article_list.html')
    article_list = Article.objects.all().order_by('date').reverse()
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

def get_article(request, article_id):
    art = get_object_or_404(Article, pk=article_id)
    return render(request, 'article.html', {'article_entity': ArticleEntity(art)})
