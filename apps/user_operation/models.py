# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from  datetime import datetime
from django.db import models
from goods.models import Goods
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFav(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(User, verbose_name=u'用户')
    goods = models.ForeignKey(Goods, verbose_name='商品')
    add_time = models.DateTimeField(u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user.name


class UserLeavingMessage(models.Model):
    MESSAGE_CHOICES = (
        (1, '留言'),
        (2, '投诉'),
        (3, '讯问'),
        (4, '售后'),
        (5, '求购')
    )
    user = models.ForeignKey(User, verbose_name=u'用户')
    message_type = models.IntegerField(u'留言类型',choices=MESSAGE_CHOICES, default=1,
                                       help_text=u'留言类型:1(留言),2(投诉),3(讯问),4(售后),5(求购)')
    message = models.TextField(u'留言内容', default='', help_text=u'留言内容')
    file = models.FileField(u'上传的文件', help_text=u'上传的文件')
    subject = models.CharField(u'主题', max_length=100, default='')
    add_time = models.DateTimeField(u'添加时间', default=datetime.now)


    class Meta:
        verbose_name = u'用户留言'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.subject


class UsrAddress(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户')
    district = models.CharField(u'区域', max_length=100, default='')
    address = models.CharField(u'用户地址', max_length=100, default='')
    signer_name = models.CharField(u'签收人', max_length=30, default='')
    signer_mobile = models.CharField(u'签收手机', max_length=11, default='')
    add_time = models.DateTimeField(u'添加时间', default=datetime.now)

    class Meta:
        verbose_name = u'用户地址'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.address

