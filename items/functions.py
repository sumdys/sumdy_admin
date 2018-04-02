#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sumdy'
from items.models import *

# 商品分类处理
# param dict data 商品分类数据
def itemTypeList(data):
    resultData = []
    parentIds = []
    subTypeData = {}
    # 获取父级ID
    for v in data:
        parentIds.append(v.id)
    # 获取子分类
    if parentIds:
        subTypeData = subItemTypeList(parentIds)
    for vo in data:
        parentData = {}
        if vo.pid==0:
            parentData['id']=vo.id
            parentData['title']=vo.title
            parentData['state']='正常' if vo.status==0 else '删除'
            parentData['status']=vo.status
            parentData['create_time']=vo.create_time
            parentData['icon'] = vo.icon
            parentData['subType'] = []
            # 二级分类
            for sub in subTypeData:
                subData = {}
                if sub['pid']==vo.id:
                    subData['id'] = sub['id']
                    subData['title'] = sub['title']
                    subData['state'] = '正常' if sub['status'] == 0 else '删除'
                    subData['status'] = sub['status']
                    subData['create_time'] = sub['create_time']
                    subData['icon'] = sub['icon']
                    parentData['subType'].append(subData)
            resultData.append(parentData)
    return resultData

# 二级分类
# param list parentIds 父级ID
# author hesheng
# 2018.3.23
def subItemTypeList(parentIds):
    res = item_type.objects.filter(pid__in=parentIds).values('id','pid','title','status','create_time','icon')
    return res
