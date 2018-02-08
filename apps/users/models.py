# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    用户
    """
    GENDER = (
        ('male', u'男'),
        ('female', u'女')
    )
    name = models.CharField(u'姓名', max_length=30, null=True, blank=True)
    birthday = models.DateField(u'出生日期', null=True, blank=True)
    mobile = models.CharField(u'手机号', max_length=11)
    gender = models.CharField(u'性别', choices=GENDER, default='male', max_length=6)
    user_email = models.EmailField(u'邮箱', max_length=100, null=True, blank=True, default='')

    class Meta:
        verbose_name = u"用户"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(u'验证码', max_length=10)
    mobile = models.CharField(max_length=11, verbose_name=u'电话')

    add_time = models.DateTimeField(u'添加事件', default=datetime.now)

    class Meta:
        verbose_name = u"短信验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.code
