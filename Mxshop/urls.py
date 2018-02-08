# coding:utf8
"""Mxshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth import settings

from django.views.static import serve

from rest_framework.documentation import include_docs_urls

import xadmin
xadmin.autodiscover()


from xadmin.plugins import xversion
xversion.register_models()


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # 后台管理
    url(r'^xadmin/', include(xadmin.site.urls)),
    # 富文本编辑
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    url(r'^goods/list/', include('goods.urls', namespace='goods')),

    # 使用drf自带文档系统
    url(r'^docs/', include_docs_urls(title='暮雪')),
]
