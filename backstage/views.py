from django.shortcuts import render
from backstage.functions import *
from minicms.functions import *
# Create your views here.

from backstage.models import *


# 后台管理菜单
def menu(request):
    page_name = '菜单管理'
    menu_list = getBackstageMenus()
    return render(request,'Menu/menu.html',{'page_name':page_name,'data':menu_list})


# 添加菜单
def menu_add(request):
    if request.method=='POST':
        name = request.POST.get('name')
        pid = request.POST.get('pid')
        menu_url = request.POST.get('menu_url')
        sort = request.POST.get('sort')
        menuId = request.POST.get('menu_id',0)
        if not name:
            return ajaxReturnError('请输入菜单名',400)
        if not menu_url:
            return ajaxReturnError('请输入地址url', 400)
        if not pid:
            level = 1
        else:
            level = Menu.objects.using('backstage').filter(id=pid).values_list('level',flat=True)
        menu = Menu.objects.using('backstage').filter(name=name)
        if not menuId and menu:
            return ajaxReturnError('菜单已存在', 400)
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
                menu.level = level[0]+1
                # print(menu.level)
                menu.save(using='backstage')
                if menu.id:
                    return ajaxReturnSuccess('提交成功')
            # except :
                return ajaxReturnError('菜单已存在', 400)
    page_name = '添加菜单'
    menus = getBackstageMenus()
    return render(request,'Menu/menu_add.html',{'page_name':page_name,'menus':menus})


#菜单信息
def menu_info(request,id):
    if not id:
        return jaxReturnError('参数不正确', 400)
    menus = getBackstageMenus()
    menuInfo = Menu.objects.using('backstage').get(id=id)
    pageName = '编辑菜单'
    return render(request,'Menu/menu_add.html',{'page_name':pageName,'data':menuInfo,'menus':menus})

# 后台管理角色
def role(request):
    where_str = {}
    keyword = request.GET.get('keyword', '')
    if keyword:
        where_str['name__contains'] =keyword
    m = Role.objects.using('backstage')
    data=resultContent(m,where_str,request)
    # 分页
    pageString = pages(request,data['pagination']['allCounts'],data['pagination']['page'],data['pagination']['pageSize'])
    page_name = '角色管理'
    roleType = getRoleType()
    for item in data['list']:
        item.type = str(item.type)
    return render(request,'Role/role.html',{'page_name':page_name,'lists':data['list'],'pageString':pageString,'roleType':roleType})


# 后台管理角色添加
def role_add(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        type = request.POST.get('type')
        roleId = request.POST.get('role_id',0)
        if roleId:
            role = Role.objects.using('backstage').get(id=roleId)
        else:
            role = Role()
        role.name = name
        role.type = type
        role.save(using='backstage')
        if role.id:
            # return JsonResponse({'code': 0, 'success': 'true', 'msg': '提交成功'})
            return ajaxReturnSuccess('提交成功')
    page_name = '添加角色'
    roleType = getRoleType()
    return render(request,'Role/role_add.html',{'page_name':page_name,'roleType':roleType})


# 编辑角色
def role_edit(request,id):
    if not id:
        return jaxReturnError('参数不正确', 400)
    roleType = getRoleType()
    Info = Role.objects.using('backstage').get(id=id)
    Info.type = str(Info.type)
    pageName = '编辑角色'
    return render(request,'Role/role_add.html',{'page_name':pageName,'data':Info,'roleType':roleType})