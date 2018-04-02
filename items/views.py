from time import time
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from minicms.functions import *
from items.functions import *
from items.models import *
from django.db import connection
import random
# Create your views here.

#商品模板管理
def item_template(request):
    page_name = '商品模板管理'
    return render(request,'item_template.html',{'page_name':page_name})

# 添加商品模板
def item_template_add(request):
    itemUnit = item_unit.objects.filter(status=1).values('id','title')
    print(itemUnit)
    page_name = '添加商品模板'
    if request.method == 'POST':
        template_id = request.POST.get('template_id')
        name = request.POST.get('name')
        type_id = request.POSt.get('type_id')
        unit_id = request.POSt.get('unit_id')
        if template_id:
            itemTemplate = item_template.objects.get(id=template_id)
        else:
            itemTemplate = item_template()
            itemTemplate.define_code = 'G',time(),random.randint(10, 99)
        itemTemplate.name = name
        itemTemplate.typy_id = type_id
        itemTemplate.unit_id = unit_id
        itemTemplate.ascription_type = 1
        itemTemplate.uploaders_passport_id =request.session['user_id']
        id = itemTemplate.save()
        if id:
            img = request.POST.get('img')
            image_url = uploadFiles(img)
    return render(request,'template_add.html',{'page_name':page_name,'itemUnit':itemUnit})

# 商品分类管理
def item_type_list(request):
    where_str = {}
    keyword = request.GET.get('keyword','')
    if keyword:
        where_str['title__contains']=keyword
    where_str['pid']=0

    m = item_type.objects
    data = resultContent(m,where_str,request)
    # 分页
    pageString = pages(request, data['pagination']['allCounts'], data['pagination']['page'], data['pagination']['pageSize'])
    data = itemTypeList(data['list'])
    page_name = '商品分类管理'
    return render(request,'item_type.html',{'page_name':page_name,'pageString':pageString,'data':data})


#添加商品分类
def item_type_add(request):
    parentType = item_type.objects.filter(pid=0).values('id','title')
    page_name = '添加商品分类'
    if request.method == 'POST':
        try:
            type_id = request.POST.get('type_id')
            name = request.POST.get('name')
            pid = request.POST.get('pid')
            if type_id:
                itemType = item_type.objects.get(id=type_id)
            else:
                itemType = item_type()
            itemType.title = name
            itemType.pid =pid
            itemType.ascription_type = 1
            itemType.save()
            if itemType.id:
                img = request.POST.get('img')
                try:
                    img.index('base64,')
                    image_url = uploadFiles(img,'items/')
                    item_type.objects.filter(id=itemType.id).update(image=image_url,icon=image_url)
                    return ajaxReturnSuccess('提交成功')
                except Exception:
                    return ajaxReturnSuccess('提交成功')
        except ValueError:
            return ajaxReturnError('提交失败')
        except Exception:
            return ajaxReturnError('提交失败')
    return render(request,'items_type_add.html',{'page_name':page_name,'parentType':parentType})

# 编辑商品类型
def item_type_edit(request,id):
    if not id:
        return jaxReturnError('参数不正确', 400)
    Info = item_type.objects.get(id=id)
    Info.pid = int(Info.pid)
    parentType = item_type.objects.filter(pid=0).values('id', 'title')
    pageName = '编辑商品类型'
    return render(request,'items_type_add.html',{'page_name':pageName,'data':Info,'parentType':parentType})

# 删除商品分类
@csrf_exempt
def itemTypeStatus(request,id,status):
    data = item_type.objects.get(id=id)
    if not data:
        return ajaxReturnError('商品类型不存')

    data.status = status
    data.save()
    print(connection.queries)
    if data.id:
        if data.pid==0:
            row = item_type.objects.filter(pid=data.id).update(status=status)
            if not row:
                return ajaxReturnError('操作子类失败')
        return ajaxReturnSuccess('操作成功')
    else:
        return ajaxReturnError('操作失败')