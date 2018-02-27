# coding:utf-8

from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

import re
from Mxshop.settings import REGEX_MOBILE
from .models import VerifyCode
from rest_framework.validators import UniqueValidator


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


class UserSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=4, min_length=4,
                                 help_text="验证码", error_messages={
            "blank": "请输入验证码",
            "required":"请输入验证码",
            "max_length":"验证码格式错误",
            "min_length":"验证码格式错误"
        })
    username = serializers.CharField(required=True, allow_blank=True,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])

    def validate_code(self, code):
        verify_recodes = VerifyCode.objects.filter(mobile=self.initial_data['username']).order_by('-add_time')
        if verify_recodes:
            last_recodes = verify_recodes[0]
            five_minute_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            if five_minute_ago<last_recodes.add_time:
                raise serializers.ValidationError("验证码过期")
            if last_recodes.code != code:
                raise serializers.ValidationError("验证码错误")

        else:
            raise serializers.ValidationError("验证码错误")

    def validate(self, attrs):
        attrs['mobile'] = attrs['username']
        del attrs['code']
        return attrs

    class Meta:
        model = User
        fields = ("username", "code", "mobile")
