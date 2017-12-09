# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import models

from DjangoUeditor.models import UEditorField


class GoodsCategory(models.Model):
    """
    商品类别
    """
    CATEGORY_TYPE = (
        (1, u'一级类目'),
        (2, u'二级类目'),
        (3, u'三级类目')
    )

    name = models.CharField(u'类别名', default='', max_length=30, help_text='类别名')
    code = models.CharField(u'类别code', max_length=30, default='', help_text='类别code')
    desc = models.TextField(u'类别描述', help_text=u'类别描述', default='')
    category_type = models.CharField(u'类目级别', choices=CATEGORY_TYPE, help_text=u'类目级别', default=1, max_length=1)
    # 自己外键自己
    parent_category = models.ForeignKey('self', null=True, blank=True, verbose_name=u'父类目级别', related_name='sub_cat')
    is_tab = models.BooleanField(u'是否导航', default=False, help_text=u'是否导航')
    add_time = models.DateTimeField(u'添加时间',default=datetime.now)

    class Meta:
        verbose_name = '商品类别'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    """

    """
    name = models.CharField(u'品牌名', help_text=u'', max_length=30,default='')
    desc = models.TextField(u'品牌描述', help_text=u'', max_length=200,default='')
    image = models.ImageField(upload_to='brands/', max_length=200)
    add_time = models.DateTimeField(u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Goods(models.Model):
    """
    商品
    """

    category = models.ForeignKey(GoodsCategory,  verbose_name=u'商品类目')
    goods_sn = models.CharField(u'商品唯一货号', max_length=50, default='')
    name = models.CharField(u'商品名', max_length=300)
    click_num = models.IntegerField(u'点击数', default=0)
    sold_num = models.IntegerField(u'销售量', default=0)
    fav_num = models.IntegerField(u'收藏数', default=0)
    goods_num = models.IntegerField(u'库存数', default=0)
    market_price = models.FloatField(u'市场价格', default=0)
    shop_price = models.FloatField(u'本店价格', default=0)
    goods_brief = models.TextField(u'商品剪短描述', max_length=500)
    goods_desc = UEditorField(u'内容', imagePath='goods/images/', height=100, width=1000, default='', filePath='goods/files/')
    ship_free = models.BooleanField(u'是否承担运费', default=True)
    goods_front_image = models.ImageField(u'封面图', upload_to='goods/images/',null=True, blank=True)
    is_new = models.BooleanField(u'是否新品',default=False)
    is_hot = models.BooleanField(u'是否热销', default=False)
    add_time = models.DateTimeField(u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = u'商品'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class GoodsImage(models.Model):
    """
    商品轮播图
    """

    goods = models.ForeignKey(Goods, verbose_name=u'商品')
    image = models.ImageField(u'图片', upload_to='goods/images、', null=True, blank=True, max_length=100)
    image_url = models.CharField(u'图片URL', max_length=300, null=True, blank=True)
    add_time = models.DateTimeField(u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = u'商品轮播图'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.goods.name


class Banner(models.Model):
    """
    轮播的商品
    """
    goods = models.ForeignKey(Goods,verbose_name=u'商品')
    image = models.ImageField(u'轮播图', upload_to='banner', max_length=300)
    index= models.IntegerField(u'轮播顺序', default=0)
    add_time = models.DateTimeField(u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = u'轮播的商品'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.goods.name

