# coding:utf-8

from rest_framework import generics
import django_filters
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    min_price = django_filters.NumberFilter(name="shop_price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(name="shop_price", lookup_expr='lte')
    name = django_filters.CharFilter(name='name', lookup_expr='contains')

    class Meta:
        model = Goods
        fields = ['min_price', 'max_price', 'name']
