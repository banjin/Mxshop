# coding:utf-8

from rest_framework import serializers
from .models import Goods, GoodsCategory


# class GoodsSerializer(serializers.Serializer):
#     click_num = serializers.IntegerField(default=0)
#     name = serializers.CharField(required=True, allow_blank=True, max_length=100)
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Goods.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance


class GoodsCategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsCategorySerializer2(serializers.ModelSerializer):
    sub_cat = GoodsCategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsCategorySerializer(serializers.ModelSerializer):
    sub_cat = GoodsCategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = GoodsCategorySerializer()
    class Meta:
        model = Goods
        fields = "__all__"

