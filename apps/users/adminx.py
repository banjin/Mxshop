# coding:utf-8

import xadmin
from xadmin import views
from .models import VerifyCode


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "慕学后台管理系统"
    site_footer = "慕课教育网"
    # 改变应用列表的展现形式
    menu_style = "accordion"


class VerifyCodeAdmin(object):
    list_display = ('code', 'mobile', 'add_time')
    search_fields = ('code', 'mobile')
    list_filter = ('code', 'mobile',  'add_time')


xadmin.site.register(VerifyCode,VerifyCodeAdmin)
# 注册主题
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
