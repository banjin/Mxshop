# coding:utf-8
import xadmin

from .models import GoodsCategory, GoodsCategoryBrand, Goods, GoodsImage,Banner


class GoodsAdmin(object):
    list_display = ('name', 'category', 'goods_sn', 'sold_num','goods_front_image', 'goods_num', 'market_price', 'fav_num', 'shop_price', 'click_num', 'add_time')
    search_fields = ('name', 'category', 'goods_sn', 'sold_num', 'goods_front_image','goods_num', 'market_price', 'shop_price', 'click_num')
    list_filter = ('name', 'category', 'goods_sn', 'sold_num', 'goods_front_image', 'goods_num', 'market_price', 'fav_num', 'shop_price', 'click_num', 'add_time')


class GoodsImageAdmin(object):
    list_display = ('goods', 'image', 'add_time', 'image_url')
    search_fields = ('goods', 'image', 'image_url')
    list_filter = ('goods__name', 'image', 'add_time')


class BannerAdmin(object):
    list_display = ('goods', 'image', 'index', 'add_time')
    search_fields = ('goods', 'image')
    list_filter = ('goods__goods_sn', 'image', 'index', 'add_time')


class GoodsCategoryBrandAdmin(object):
    list_display = ('image', 'desc', 'name', 'add_time')
    search_fields = ('image', 'desc', 'name')
    list_filter = ('image', 'desc', 'name', 'add_time')


class GoodsCategoryAdmin(object):
    list_display = ('code', 'desc', 'name', 'category_type', 'is_tab', 'add_time')
    search_fields = ('code', 'desc', 'category_type', 'is_tab', 'name')
    list_filter = ('code', 'desc', 'name', 'category_type', 'is_tab', 'add_time')

xadmin.site.register(Goods,GoodsAdmin)
xadmin.site.register(GoodsImage, GoodsImageAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(GoodsCategoryBrand, GoodsCategoryBrandAdmin)
xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)

