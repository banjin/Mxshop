# coding:utf-8

from django.conf.urls import url
from base_views import GoodsListView
from .views import GoodsList
urlpatterns = [
    url(r'^$', GoodsListView.as_view(), name='goods_list'),
    url(r'^api/$', GoodsList.as_view()),
]