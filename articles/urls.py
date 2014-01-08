'''
Created on Jan 6, 2014

@author: Kyle Rogers
'''
from django.conf.urls import patterns, url

from articles import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^service/$', views.service, name='service'),
    url(r'^pd/$', views.professional_development, name='professional_development'),
    url(r'^social/$', views.social, name='social'),
    url(r'^(?P<article_id>\d+)', views.get_article, name='article'),
    url(r'^service/(?P<article_id>\d+)', views.get_article, name='article'),
    url(r'^pd/(?P<article_id>\d+)', views.get_article, name='article'),
    url(r'^social/(?P<article_id>\d+)', views.get_article, name='article'),
)