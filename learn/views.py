from django.shortcuts import render
from django.http import HttpResponse
from urllib import request,parse
from http import cookiejar

from learn.models import *
from .functions import *
from .forms import *

import os,random

# Create your views here.
def index(request):
    # users = Users.objects.all()
    if request.method == 'POST':
        form = AddForm(request.POST,request.FILES)
        if form.is_valid():#验证数据是否合法，当合法时可以使用cleaned_data属性。
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            realName = form.cleaned_data['real_name']
            headUrl = form.cleaned_data['headImg']
            addr = form.cleaned_data['addr']
            email = form.cleaned_data['email']
            # 上传文件保存
            file_path = os.path.join('learn/upload/',headUrl.name)
            fp =open(file_path,'wb+')
            s = headUrl.read()
            fp.write(s)
            fp.close()
            # 保存数据
            users = Users()
            users.name=username
            users.real_name =realName
            users.password = md5Function(password)
            users.addr = addr
            users.email =email
            users.head_url =headUrl
            res = users.save()
            print(headUrl)
            print(username)
            return HttpResponse('OK',res)
    else:
        form = AddForm()

    return render(request,'index.html',{'form':form})


def register(request):
    if request.method == 'POST':
        uf = RegisterForm(request.POST,request.FILES)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            realName = uf.cleaned_data['real_name']
            password = uf.cleaned_data['password']
            addr = uf.cleaned_data['addr']
            email = uf.cleaned_data['email']
            headImg = uf.cleaned_data['head_url']
            # 上传文件
            # file_path = os.path.join('learn/upload/',headImg.name)
            # fp = open(file_path,'wb+')
            # s=headImg.read()
            # fp.write(s)
            # fp.close()
            # 添加数据
            userModel = Users()
            userModel.name = username
            userModel.real_name = realName
            userModel.password = md5Function(password)
            userModel.addr = addr
            userModel.email = email
            userModel.head_url = headImg
            userModel.save()

            print(headImg)
            return HttpResponse('OK')

    else:
        uf = RegisterForm()
    return render(request,'register.html',{'form':uf})



def loadImage(request):
    headers = {
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    c = cookiejar.CookieJar()
    #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    handler = request.HTTPCookieProcessor(c)
    #通过CookieHandler创建opener
    opener = request.build_opener(handler)
    request.install_opener(opener)
    url = 'http://oss.0085.com/2017/0426/supplychaint/14932009270987.jpeg'
    reqImage = request.Request(url)
    reqImage.headers = headers
    codeImg = opener.open(reqImage).read()
    fn = open('14932009270987.jpeg', 'wb+')
    fn.write(codeImg)
    fn.close()

    return HttpResponse('OK')