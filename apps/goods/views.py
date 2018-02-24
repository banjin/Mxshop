# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Goods
from .serializers import GoodsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from rest_framework.filters import SearchFilter

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from goods.filters import GoodsFilter


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = 'p'


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
    '''
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer   
    # pagination_class = LargeResultsSetPagination
    # filter_backends = (DjangoFilterBackend,)
    filter_backends = (SearchFilter,)
    # filter_class = GoodsFilter
    search_fields = ('name', 'goods_desc')



