#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date: 2019/10/8 17:37
# Author: ZuoJie
# Version: 1.0
import xadmin
from app01.models import MovieInfo
from xadmin import views


# 然后我们需要创建class，class命名格式最好为类名+Admin
class RtStudentAdmin:
    list_display = ['no', 'url', 'title', 'desc', 'grade']
    # list_editable = ['no', 'url', 'title', 'desc', 'grade']
    search_fields = ['no', 'url', 'title', 'desc', 'grade']


class GlobalSetting(object):
    site_title = '世界电影排行榜'  # 设置头标题
    site_footer = '世界电影排行榜'  # 设置脚标题
    menu_style = 'accordion'  # 可收缩列


class BaseSetting(object):
    #  开启主题
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(MovieInfo, RtStudentAdmin)
