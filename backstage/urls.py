#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sumdy'

from django.conf.urls import url
from backstage import views as backstage_views


urlpatterns = [
    # 后台系统设置
    url(r'menu/$',backstage_views.menu),
    url(r'menu_add/$',backstage_views.menu_add),
    url(r'menu_info/(\d+)',backstage_views.menu_info),
    url(r'role/$',backstage_views.role),
    url(r'role_add/$', backstage_views.role_add),
    url(r'role_edit/(\d+)',backstage_views.role_edit),
]