#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sumdy'


from django.conf.urls import url,include
from django.contrib import admin
from items import views as items_views
admin.autodiscover()


urlpatterns = [
    url(r'template/$',items_views.item_template),
    url(r'template_add/$',items_views.item_template_add),
    url(r'type/$',items_views.item_type),
    url(r'type_add/$',items_views.item_type_add),
]