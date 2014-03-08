from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import Context, loader
from django.db.models import Q
import math

from articles.models import Article, ArticleEntity
from listing.pages import PageHelper

default_count_per_page = 5
max_count_per_page = 25
max_pages_listed_on_screen = 5
 
def general_listing(request, eventType, category):
    t = loader.get_template('article_list.html')
    category_query = Q()
    if category != None:
        category_query = Q(category__name=category)
    article_list = Article.objects.filter(category_query).order_by('date').reverse()
    article_count = PageHelper.get_request_count(request, default_count_per_page, max_count_per_page)
    page_number = PageHelper.get_page_number(request)
    articles_range_min = (page_number - 1) * article_count
    articles_range_max = (page_number) * article_count    
    number_of_articles = len(article_list)
    total_pages = int(math.ceil(number_of_articles / float(article_count)))
    article_list = article_list[articles_range_min:articles_range_max]
    page_numbers_list = PageHelper.calculate_page_range(total_pages, page_number, max_pages_listed_on_screen)    
    next_page = page_number + 1 if number_of_articles > articles_range_max else 0
    prev_page = page_number - 1
    context_dict = {
                    'eventType': eventType,
                    'article_list' : article_list,
                    'article_count': article_count, 
                    'page_number' : page_number, 
                    'prev_page': prev_page, 
                    'next_page' : next_page, 
                    'page_numbers' : page_numbers_list
                    }
    c = Context(context_dict)
    return HttpResponse(t.render(c))

def index(request):
    return general_listing(request, 'All', None)    
 
def service(request):
    return general_listing(request, 'Service', 'Service')

def professional_development(request):
    return general_listing(request, 'Professional Development', 'PD')

def brotherhood(request):
    return general_listing(request, 'Brotherhood', 'Brotherhood')

def get_article(request, article_id):
    art = get_object_or_404(Article, pk=article_id)
    return render(request, 'article.html', {'article_entity': ArticleEntity(art), 'pictures': art.gallery.pictures.all })
