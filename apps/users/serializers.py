# coding:utf-8

from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

import re
from Mxshop.settings import REGEX_MOBILE
from .models import VerifyCode


from datetime import datetime, timedelta
class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param data:
        :return:
        """
        # 手机是否注册
        if User.objects.filter(mobile=mobile).exists():
            raise serializers.ValidationError("手机号码已经注册")

        # 手机格式是否正确
        if not re.match(REGEX_MOBILE,mobile):
            raise serializers.ValidationError("手机号码不正确")

        # 验证码发送频率
        one_minutes_ago = datetime.now() - timedelta(minutes=1)
        if VerifyCode.objects.filter(add_time__gt=one_minutes_ago, mobile=mobile).exists():
            raise serializers.ValidationError("验证码已经发送")

        return mobile
