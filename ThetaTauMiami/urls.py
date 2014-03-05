from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'marketing.views.greetings'),
    url(r'^splash/$', 'marketing.views.splash'),
    url(r'^default/$', 'marketing.views.index'),
    url(r'^contact/$', 'marketing.views.contact'),
    url(r'^tools/$', 'marketing.views.upcoming_page'),
    url(r'^events/$', 'marketing.views.calendar'),
    url(r'^info/', include('info.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
