from django.shortcuts import render
from items.functions import *

# Create your views here.

#商品模板管理
def item_template(request):
    page_name = '商品模板管理'
    return render(request,'item_template.html',{'page_name':page_name})

# 商品分类管理
def item_type(request):
    page_name = '商品分类管理'
    
    return render(request,'item_type.html',{'page_name':page_name})


#添加商品分类
def item_type_add(request):
    page_name = '添加商品分类'
    if request.method == 'POST':
        pid = request.POST.get('parent_id')
        name = request.POST.get('name')
        img = request.POST.get('img')
        image_url = uploadFiles(img)
    return render(request,'items_type_add.html',{'page_name':page_name})

