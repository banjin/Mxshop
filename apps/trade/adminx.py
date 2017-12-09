# coding:utf-8
import xadmin

from .models import ShoppingCart, OrderInfo, OrderGoods


class OrderInfoAdmin(object):
    list_display = ('user', 'order_sn', 'trade_no', 'pay_status','order_mount', 'address', 'post_script', 'singer_name', 'singer_mobile', 'add_time')
    search_fields = ('user', 'order_sn', 'trade_no', 'pay_status', 'order_mount','address', 'post_script', 'singer_name', 'singer_mobile')
    list_filter = ('user__name', 'order_sn', 'trade_no', 'pay_status', 'order_mount', 'address', 'post_script', 'singer_name', 'singer_mobile',  'add_time')


class OrderGoodsAdmin(object):
    list_display = ('order', 'goods_num', 'goods', 'add_time')
    search_fields = ('order', 'goods_num', 'goods')
    list_filter = ('order__order_sn', 'goods_num', 'goods__name', 'add_time')


class ShoppingCartAdmin(object):
    list_display = ('user', 'goods', 'good_num', 'add_time')
    search_fields = ('user', 'goods', 'good_num')
    list_filter = ('user__name', 'goods__name', 'good_num', 'add_time')

xadmin.site.register(OrderInfo,OrderInfoAdmin)
xadmin.site.register(OrderGoods, OrderGoodsAdmin)
xadmin.site.register(ShoppingCart, ShoppingCartAdmin)
