#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sumdy'
from django.http import JsonResponse
from django.conf import settings
import math

# 获取查询数据
def resultContent(models,request):
    where_str = {}
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    pageSize = int(request.GET.get('page_size',settings.PAGE))
    keyword = request.GET.get('keyword','')
    startPos = (page - 1)*pageSize
    endPos = startPos + pageSize
    if keyword:
        where_str['name__contains']="%s" % keyword
    resList = models.filter(**where_str).order_by('id')[startPos:endPos]
    # print(resList.query)
    # 总数
    allCounts = models.filter(**where_str).count()
    res={}
    pagination = {}
    pagination['allCounts']=allCounts
    pagination['page']=page
    pagination['pageSize']=pageSize
    res['pagination'] =pagination
    res['list'] = resList
    return res

# 分页
# @param allPostCounts int 总记录数
# @param page int 当前页码
# @param pageSize int 当前每页显示数
# @author hesheng
# 2018.2.5
def pages(request,allPostCounts,page,pageSize=0):
    param = ''
    if request.GET:
        for key,value in request.GET.items():
            if key not in ['page','page_size']:
                param+='&'+key+'=%s' % value
        print(param)
    page_list = []
    # 首页，上一页
    if page == 1:
        first = ""
        prev = ''
    else:
        first = "<li><a href='?page=1&page_size=%s%s'>首页</a></li>" % (pageSize,param)
        prev = '<li><a href="?page=%s&page_size=%s%s" aria-label="Previous"><span aria-hidden="true">上一页</span></a></li>' % (page-1,pageSize,param)
    page_list.append(first)
    page_list.append(prev)

    # 总页数
    allPages = math.ceil(allPostCounts / pageSize)
    for p in range(1,allPages+1):
        if p == page:
            temp = "<li class='active'><a href='?page=%spage_size=%s%s'>%s</a></li>" % (p, pageSize,param,p)
        else:
            temp = "<li><a href='?page=%s&page_size=%s%s'>%s</a></li>" % (p,pageSize,param, p)
        page_list.append(temp)

    # 下一页，尾页
    if page == allPages:
        last = ""
        nex = ''
    else:
        last = "<li><a href='?page=%s&page_size=%s%s'>尾页</a></li>" % (allPages, pageSize,param)
        nex = '<li><a href="?page=%s&page_size=%s%s" aria-label="Next"><span aria-hidden="true">下一页</span></a></li>' % (page + 1,pageSize,param)
    page_list.append(nex)
    page_list.append(last)

    return ''.join(page_list)


# 成功返回
def ajaxReturnSuccess(msg):
    data = {}
    data['code']=0
    data['success']='true'
    data['msg']=msg
    return JsonResponse(data)

# 失败返回
def ajaxReturnError(msg,errorCode=400):
    return JsonResponse({'code': errorCode, 'success': 'true', 'msg': msg})