from django.shortcuts import render
from django.http import JsonResponse
from backstage.functions import *
from django.conf import settings
# Create your views here.

from backstage.models import *
import os

# 后台管理菜单

def backstage_menu(request):
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    pageSize = int(request.GET.get('page_size',settings.PAGE))
    # pageSize = settings.PAGE if not page_size else page_size
    startPos = (page - 1)*pageSize
    endPos = startPos + pageSize
    menu_list = Menu.objects.using('backstage').all().order_by('id')[startPos:endPos]
    # 总数
    allCounts = Menu.objects.using('backstage').count()
    # 分页
    pagestring = pages(allCounts,page,pageSize)
    page_name = '菜单管理'
    return render(request,'backstage_menu.html',{'page_name':page_name,'data':menu_list,'pagestring':pagestring})

# 添加菜单
def backstage_menu_add(request):
    if request.method=='POST':
        name = request.POST.get('name')
        pid = request.POST.get('pid')
        menu_url = request.POST.get('menu_url')
        sort = request.POST.get('sort')
        menuId = request.POST.get('menu_id',0)
        if not name:
            return JsonResponse({'code':400,'msg':'请输入菜单名'})
        if not menu_url:
            return JsonResponse({'code':400,'msg':'请输入地址url'})
        if not pid:
            level = 1
        else:
            level = Menu.objects.using('backstage').filter(id=pid).values_list('level',flat=True)
        menu = Menu.objects.using('backstage').filter(name=name,url=menu_url)
        if not menuId and menu:
            return JsonResponse({'code': 400, 'msg': '菜单已存在'})
        else:
            # try:
                if menuId:
                    menu = Menu.objects.using('backstage').get(id=menuId)
                else:
                    menu = Menu()
                menu.name = name
                menu.pid = pid if pid else 0
                menu.url = menu_url
                menu.sort = int(sort)
                menu.level = level[0]
                menu.save(using='backstage')
                if menu.id:
                    return JsonResponse({'code':0,'success':'true','msg':'提交成功'})
            # except :
                return JsonResponse({'code': 400, 'msg': '菜单已存在'})
    page_name = '添加菜单'
    return render(request,'backstage_menu_add.html',{'page_name':page_name})

#菜单信息
def backstage_menu_info(request,id):
    if not id:
        return JsonResponse({'code':400,'msg':'参数不正确'})
    res = getLevelMenu()
    print(res)
    menuInfo = Menu.objects.using('backstage').get(id=id)
    pageName = '编辑菜单'
    return render(request,'backstage_menu_add.html',{'page_name':pageName,'data':menuInfo})

# 后台管理角色
def backstage_role(request):
    page_name = '角色管理'
    return render(request,'backstage_role.html',{'page_name':page_name})