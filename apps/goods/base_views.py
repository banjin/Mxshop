# coding:utf-8

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.generic.base import View

from django.forms.models import model_to_dict

from django.core import serializers

# from django.views.generic import ListView
from .models import Goods


class GoodsListView(View):
    """
    商品列表, 通过django的view实现商品列表页
    """

    def get(self, request):
        json_list = []
        goods_list = Goods.objects.all()[:3]
        # for good in goods_list:
            # goods_json = {}
            # goods_json['name'] = good.name
            # goods_json['category'] = good.category.name
            # json_list.append(goods_json)
            # or
            # json_list.append(model_to_dict(good))
        # 返回json格式数据，但是有些字段不能直接转成json
        # return HttpResponse(json.dumps(json_list), content_type='application/json')

        # 使用Django内部的序列化方法对数据进行序列化
        json_data = serializers.serialize("json", goods_list)
        json_data = json.loads(json_data)
        # return HttpResponse(json.dumps(json_data), content_type='application/json')
        return JsonResponse(json_data, safe=False)


