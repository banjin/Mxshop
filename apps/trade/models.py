# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model
from goods.models import Goods

from users.models import UserProfile

UserModel = get_user_model()


class ShoppingCart(models.Model):
    """
    购物车
    """
    user = models.ForeignKey(UserModel, verbose_name=u'用户')

    goods = models.ForeignKey(Goods, verbose_name=u'商品')
    good_num = models.IntegerField(u'购买数量', default=0)
    add_time = models.DateTimeField(u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = u'购物车'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return "%s(%d)".format(self.goods.name, self.good_num)


class OrderInfo(models.Model):
    """
    订单
    """
    ORDER_STATUS = (
        ('success', '成功'),
        ('cancel', '取消'),
        ('cancel', '待支付')
    )

    user = models.ForeignKey(UserModel, verbose_name=u'用户')
    order_sn = models.CharField(u'订单编号', unique=True, max_length=100)
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True)
    pay_status = models.CharField(u'订单状态', max_length=10, choices=ORDER_STATUS, default='')
    order_mount = models.FloatField(u'订单金额', default=0.0)
    pay_time = models.DateTimeField(u'支付时间', null=True, blank=True)
    address = models.CharField(u'收货地址', default='', max_length=100)
    post_script = models.CharField(u'订单留言', max_length=200)
    singer_name = models.CharField(u'签收人', default='', max_length=20)
    singer_mobile = models.CharField(u'联系电话', max_length=11)
    add_time = models.DateTimeField(u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = u'订单'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.order_sn


class OrderGoods(models.Model):
    """
    订单商品详情
    """
    order = models.ForeignKey(OrderInfo, verbose_name=u'订单信息')
    goods = models.ForeignKey(Goods, verbose_name='商品')
    goods_num = models.IntegerField(u'商品数量', default=0)
    add_time = models.DateTimeField(u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = u'订单商品'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.order.order_sn
