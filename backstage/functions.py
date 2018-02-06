#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sumdy'
from backstage.models import *
import math

# 分页
# @param allPostCounts int 总记录数
# @param page int 当前页码
# @param pageSize int 当前每页显示数
# @author hesheng
# 2018.2.5
def pages(allPostCounts,page,pageSize=0):
    page_list = []
    # 首页，上一页
    if page == 1:
        first = ""
        prev = ''
    else:
        first = "<li><a href='?page=1&page_size=%s'>首页</a></li>" % (pageSize,)
        prev = '<li><a href="?page=%s&page_size=%s" aria-label="Previous"><span aria-hidden="true">上一页</span></a></li>' % (page-1,pageSize)
    page_list.append(first)
    page_list.append(prev)

    # 总页数
    allPages = math.ceil(allPostCounts / pageSize)
    for p in range(1,allPages+1):
        if p == page:
            temp = "<li class='active'><a href='?page=%s'>%s</a></li>" % (p, p)
        else:
            temp = "<li><a href='?page=%s&page_size=%s'>%s</a></li>" % (p,pageSize, p)
        page_list.append(temp)

    # 下一页，尾页
    if page == allPages:
        last = ""
        nex = ''
    else:
        last = "<li><a href='?page=%s&page_size=%s'>尾页</a></li>" % (allPages, pageSize)
        nex = '<li><a href="?page=%s&page_size=%s" aria-label="Next"><span aria-hidden="true">下一页</span></a></li>' % (page + 1,pageSize)
    page_list.append(nex)
    page_list.append(last)

    return ''.join(page_list)


def getLevelMenu():
    menu = Menu.objects.using('backstage').filter(level__in=(1,2)).values('id','pid','name')
    # print(menu)
    data =[]
    idata =subMenu = {}
    for item in menu:
        r={}
        s = []
        if item['pid'] == 0:
            idata['id']=item['id']
            idata['name']=item['name']
            data.append(idata)
        else:
            subMenu['id']=item['id']
            subMenu['name']=item['name']
            s.append(subMenu)
            r[item['pid']]=s
            print(r)
    # return data
