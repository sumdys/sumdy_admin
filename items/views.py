from time import time
from django.shortcuts import render
from items.functions import *
from items.models import *
import random
# Create your views here.

#商品模板管理
def item_template(request):
    page_name = '商品模板管理'
    return render(request,'item_template.html',{'page_name':page_name})

# 添加商品模板
def item_template_add(request):
    page_name = '添加商品模板'
    return render(request,'template_add.html',{'page_name':page_name})

# 商品分类管理
def item_type(request):
    page_name = '商品分类管理'
    return render(request,'item_type.html',{'page_name':page_name})


#添加商品分类
def item_type_add(request):
    page_name = '添加商品分类'
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
    return render(request,'items_type_add.html',{'page_name':page_name})

