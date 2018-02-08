#coding:utf-8
from django import VERSION
from views import get_ueditor_controller

if VERSION[0:2] > (1, 3) and VERSION[0:2] < (1,11):
    from django.conf.urls import patterns, url

    urlpatterns = patterns('',
                           url(r'^controller/$', get_ueditor_controller)
                           )
elif VERSION[0:2] < (1, 3):
    from django.conf.urls.defaults import patterns, url

    urlpatterns = patterns('',
                           url(r'^controller/$', get_ueditor_controller)
                           )
else:
    from django.conf.urls import url
    urlpatterns = [url(r'^controller/$', get_ueditor_controller)]

