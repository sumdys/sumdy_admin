from django.shortcuts import render

# Create your views here.

# 后台管理菜单
def backstage_menu(request):
    page_name = '菜单管理'
    return render(request,'backstage_menu.html',{'page_name':page_name})

# 添加菜单
def backstage_menu_add(request):
    page_name = '添加菜单'
    return render(request,'backstage_menu_add.html',{'page_name':page_name})

# 后台管理角色
def backstage_role(request):
    page_name = '角色管理'
    return render(request,'backstage_role.html',{'page_name':page_name})