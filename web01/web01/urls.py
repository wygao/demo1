from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web01.views.home', name='home'),
    # url(r'^web01/', include('web01.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','blog.views.index'),
    url(r'^regist/$','blog.views.regist_user'),
    #url(r'^login/$','blog.views.login_user'),
    #url(r'^tea/','blog.views.disp_tea'),
    #url(r'^cake/','blog.views.disp_cake'),
    #url(r'^logout/$','blog.views.logout_user'),
    #url(r'^order/$','blog.views.order'),
    #url(r'^pay/$','blog.views.pay'),
)
