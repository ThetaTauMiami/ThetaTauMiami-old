from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import Context, loader

from articles.models import Article, ArticleCategory, ArticleEntity, Gallery, InGallery, Picture

def index(request):
    t = loader.get_template('article_list.html')
    article_list = Article.objects.all().order_by('date').reverse()
    if len(article_list) == 0:
        article_list = None
    c = Context({'eventType': 'All', 'article_list': article_list})
    return HttpResponse(t.render(c))
 
def service(request):
    type_id = ArticleCategory.objects.filter(name="Service")[0].id
    t = loader.get_template('article_list.html')
    article_list = Article.objects.filter(category=type_id)
    c = Context({'eventType': 'Service', 'article_list': article_list})
    return HttpResponse(t.render(c))

def professional_development(request):
    type_id = ArticleCategory.objects.filter(name="PD")[0].id
    t = loader.get_template('article_list.html')
    article_list = Article.objects.filter(category=type_id)
    c = Context({'eventType': 'Professional Development', 'article_list': article_list})
    return HttpResponse(t.render(c))

def social(request):
    type_id = ArticleCategory.objects.filter(name="Social")[0].id
    t = loader.get_template('article_list.html')
    article_list = Article.objects.filter(category=type_id)
    c = Context({'eventType': 'Social', 'article_list': article_list})
    return HttpResponse(t.render(c))

def get_article(request, article_id):
    art = get_object_or_404(Article, pk=article_id)
    gal_id = art.gallery.id
    in_gals = InGallery.objects.filter(gallery=gal_id)
    pics = set()
    for in_gal in in_gals:
        pics.add(in_gal.image)
    return render(request, 'article.html', {'article_entity': ArticleEntity(art), 'pictures': pics})
