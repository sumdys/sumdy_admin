from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

from backstage.models import Menu

# 后台管理菜单

def backstage_menu(request):
    page_name = '菜单管理'
    return render(request,'backstage_menu.html',{'page_name':page_name})

# 添加菜单
def backstage_menu_add(request):
    if request.method=='POST':
        name = request.POST.get('name')
        pid = request.POST.get('pid')
        menu_url = request.POST.get('menu_url')
        sort = request.POST.get('sort')
        if not name:
            return JsonResponse({'code':400,'msg':'请输入菜单名'})
        if not menu_url:
            return JsonResponse({'code':400,'msg':'请输入地址url'})

        menu = Menu.objects.using('backstage').filter(name=name,url=menu_url)
        if menu:
            return JsonResponse({'code': 400, 'msg': '菜单已存在'})
        menu.name = name
        menu.pid = pid if pid else 0
        menu.url = menu_url
        menu.sort = int(sort)
        if menu.save(using='backstage'):
            return JsonResponse({'code':0,'msg':'success'})
    page_name = '添加菜单'
    return render(request,'backstage_menu_add.html',{'page_name':page_name})

# 后台管理角色
def backstage_role(request):
    page_name = '角色管理'
    return render(request,'backstage_role.html',{'page_name':page_name})