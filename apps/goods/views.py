# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Goods, GoodsCategory
from .serializers import GoodsSerializer, GoodsCategorySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from goods.filters import GoodsFilter


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = 'page'


"""
class GoodsList(mixins.ListModelMixin, generics.GenericAPIView):
    '''
    List all snippets, or create a new snippet.
    '''
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    # def get(self, request, format=None):
    #     goods = Goods.objects.all()[:10]
    #     serializer = GoodsSerializer(goods, many=True)
    #     return Response(serializer.data)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, format=None):
        serializer = GoodsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    List all snippets, or create a new snippet.
    分页，搜索，过滤，排序
    '''
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    # 配置局部验证，在setting中可以配置全局
    # authentication_classes = (TokenAuthentication,)
    pagination_class = LargeResultsSetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('=name', 'goods_desc', 'goods_brief')
    ordering_fields = ('sold_num', 'shop_price')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = GoodsCategorySerializer
