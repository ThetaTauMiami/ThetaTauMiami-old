'''
Created on Dec 19, 2013

@author: kyle
'''
from django.conf.urls import patterns, url

from info import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^officers/$', views.officers, name='officers'),
    url(r'^actives/$', views.actives, name='actives'),
    url(r'^pledges/$', views.pledges, name='pledges'),
    url(r'^alumni/$', views.alumni, name='alumni'),
    url(r'^brother/(?P<brother_id>\d+)', views.brother_profile, name="brother_profile"),
    url(r'^resumes/$', views.resumes, name='resumes'),
    url(r'^careers/$', views.careers, name='careers')
    
)