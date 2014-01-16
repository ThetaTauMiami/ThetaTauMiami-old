from django.shortcuts import render
from django.template import Context, loader

from django.http import HttpResponse

from articles.models import Article, ArticleEntity
from marketing.models import Picture

# Create your views here.
def index(request):
    t = loader.get_template('index.html')
    article_list = Article.objects.all().order_by('date').reverse()[:3]
    ael = []
    for a in article_list:
        ael.append(ArticleEntity(a))
    article_numbers = range(1,len(ael) + 1) # +1 because of the nationals pic, starts at one because of first_ae
    c = Context({'first_ae': ael[0], 'article_entity_list':ael[1:], 'article_numbers': article_numbers})
    return HttpResponse(t.render(c))

def contact(request):
    t = loader.get_template('contact_us.html')
    c = Context({})
    return HttpResponse(t.render(c))

def upcoming_page(request):
    t = loader.get_template('upcoming.html')
    c = Context({})
    return HttpResponse(t.render(c))