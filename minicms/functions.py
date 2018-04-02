#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sumdy'
from django.http import JsonResponse
from django.conf import settings
from base64 import b64decode
import math
import time
import os

'''
获取查询数据
@author hesheng
@param models 模型
@param where_str 查询条件
@param request 请求参数
'''
def resultContent(models,where_str,request):
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    pageSize = int(request.GET.get('page_size',settings.PAGE))
    startPos = (page - 1)*pageSize
    endPos = startPos + pageSize
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
    data['success']=True
    data['msg']=msg
    return JsonResponse(data)

# 失败返回
def ajaxReturnError(msg,errorCode=400):
    return JsonResponse({'code': errorCode, 'success': False, 'msg': msg})




#上传图片
def uploadFiles(img,dir=''):
    image_url = ''
    try:
        # 保存路经
        file_path = os.path.join('upload/images/',dir)
        # 如果目录不存在，就新建
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        # 获取base64字符串
        imageData = img.split('base64,', 1)
        # base64解码
        image_data = b64decode(imageData[1])
        # 文件后辍
        fileType = imageData[0].split('/',1)
        file_ext = '.jpg'
        if fileType=='jpeg':
            file_ext = '.jpg'
        elif fileType == 'png':
            file_ext = '.'+fileType
        # 文件名字
        image_name = str(int(time.time())) + file_ext
        file_name = file_path+image_name
        image_url = settings.IMAGES_PATH+'/'+dir+image_name
        # 上传文件保存
        with open(file_name, 'wb') as f:
            f.write(image_data)
            f.close()
    except Exception as e:
        print(e)
    return image_url
