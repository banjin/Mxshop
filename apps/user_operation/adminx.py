# coding:utf-8
import xadmin

from .models import UserFav, UserLeavingMessage, UsrAddress


class UserLeavingMessageAdmin(object):
    list_display = ('user', 'message_type', 'message', 'file', 'subject','add_time')
    search_fields = ('user', 'message_type', 'message', 'file', 'subject')
    list_filter = ('user__name', 'message_type', 'message','subject', 'file', 'add_time')


class UserFavAdmin(object):
    list_display = ('user', 'goods', 'add_time')
    search_fields = ('user', 'goods')
    list_filter = ('user__name', 'goods__goods_sn', 'add_time')


class UsrAddressAdmin(object):
    list_display = ('user', 'district', 'address', 'signer_name', 'signer_mobile', 'add_time')
    search_fields = ('user', 'district', 'address', 'signer_name', 'signer_mobile')
    list_filter = ('user__name', 'district', 'address', 'signer_name', 'signer_mobile', 'add_time')

xadmin.site.register(UserLeavingMessage,UserLeavingMessageAdmin)

xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UsrAddress, UsrAddressAdmin)

