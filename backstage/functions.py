#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sumdy'
from backstage.models import *


def getBackstageMenus():
    menu = Menu.objects.using('backstage').filter(level__in=(1,2,3)).order_by('sort').values('id','pid','name','level','url','create_time')
    menu = list(menu)
    res = []
    # print(menu)
    for item in list(menu):
        idata = {}
        if item['level'] == 1:
            idata['id']=item['id']
            idata['name']=item['name']
            idata['url'] = item['url']
            idata['create_time']=item['create_time']
            idata['submenus']=[]
            for se in list(menu):
                if se['pid'] == item['id']:
                    se['thirdMenus']=[]
                    for th in menu:
                        if th['pid']==se['id']:
                            se['thirdMenus'].append(th)
                    # print(se)
                    idata['submenus'].append(menusList(se))
            res.append(idata)
    return res


def menusList(data):
    subMenu = {}
    if data:
        for k,v in data.items():
            subMenu[k]=v
    return subMenu


# 角色类型
def getRoleType():
    type_list = {'1':'总部','2':'门店供应商','3':'平台供应商'}
    return type_list

