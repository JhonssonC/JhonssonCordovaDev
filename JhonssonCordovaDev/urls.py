# coding=utf-8
from __future__ import unicode_literals
from django.conf.urls import patterns, include, url

from django.conf.urls import patterns, include, url
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'JhonssonCordovaDev.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'principal.views.index', name='index'),
)
