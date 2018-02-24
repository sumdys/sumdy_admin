from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect

# PIL是python2版本的图像处理库，不过现在用Pillow比PIL强大，是python3的处理库
from PIL import Image,ImageDraw,ImageFont
# 在python3.x中，StringIO已经在io模块中了，导入方法
from io import BytesIO
from online.models import *
from learn.models import *
from learn.functions import *
from learn.forms import *
from backstage.functions import *

import os,random
# Create your views here.

# 认证登录



def authLogin(func):
    '''身份认证装饰器，
    :param func:
    :return:
    '''
    def wrapper(request,*args,**kwargs):
        if not request.session.get("isLogin"):
            return HttpResponseRedirect("/login/")
        return  func(request,*args, **kwargs)
    return wrapper


@authLogin
def index(request):
    username = request.session.get('username')
    menus=getBackstageMenus()
    return render(request,'online/index.html',{'username':username,'menus':menus})


def register(request):
    return render(request,'register.html')


def login(request):
    return render(request,'login.html')



def logout(request):
    request.session['isLogin']=False
    if request.session['isLogin']:
        return HttpResponseRedirect('/index/')
    else:
        return HttpResponseRedirect('/login/')



#ajax登录校验回调视图函数
def login_ajax_check(request):
    if request.method=='POST':
        #1,获取用户输入的用户名和密码
        username = request.POST.get('username')
        password = request.POST.get('password')
        #2,获取输入验证码
        vCode = request.POST.get('verifyCode')
        if not username or not password:
            return JsonResponse({'msg':'username is null Or password is null'})
        if not vCode:
            return JsonResponse({'msg':'verify code is null'})
        #3,获取session中验证码
        vCode_session = request.session.get('verifyCode')
        password = md5Function(password)
        #4,获取用户数据信息
        users = Users.objects.filter(name=username,password=password)
        if not users:
            return JsonResponse({'code': 400, 'msg': '用户名或密码不正确'})
        name=''
        passwordD =''
        for user in users:
            passwordD = user.password
            name = user.name
            break
        vCode = vCode.upper()
        # print(name)
        if username==name and password==password and vCode==vCode_session:
            # 保存用户的登录状态
            request.session['isLogin'] = True
            request.session['username'] = username
            return JsonResponse({'code':0,'msg':'ok'})
        elif username!=name or password != passwordD:
            return JsonResponse({'code':400,'msg':'用户名或密码不正确'})
        elif vCode != vCode_session:
            return JsonResponse({'code':400,'msg':'验证码错误'})
    else:
        return render(request,'login.html')



#验证码
def verify_code(request):
    # 1,定义变量，用于画面的背景色,宽,高
    # random.randrange(20, 100)意思是在20到100之间随机找一个数
    bgcolor = (random.randrange(20,100),random.randrange(20,100),255)
    width = 100
    height = 40
    # 2，创建画面对象
    im = Image.new('RGB',(width,height),bgcolor)
    if im.mode != 'RGB':
        im = im.convert('RGB')

    # 3,创建画笔对象
    draw = ImageDraw.Draw(im)
    for i in range(0,100):
        # 噪点绘制的范围
        xy = (random.randrange(0,width),random.randrange(0,height))
        # 噪点的随机颜色
        fill = (random.randrange(0,255),255,random.randrange(0,255))
        # 绘制出噪点
        draw.point(xy,fill=fill)

    # 5，定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 6，随机选取4个值作为验证码
    rand_str = ''
    for i in range(0,4):
        rand_str +=str1[random.randrange(0,len(str1))]
    # 7，构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('C:\Windows\Fonts\FreeMono.ttf',30)
    # font = ImageFont.load_default().font
    # 8，构造字体颜色
    fontColor1 = (255,random.randrange(0,255),random.randrange(0,255))
    fontColor2 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontColor3 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontColor4 = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 9，绘制4个字
    draw.text((5,4), rand_str[0], font=font, fill=fontColor1)
    draw.text((25,4), rand_str[1], font=font, fill=fontColor2)
    draw.text((50,4), rand_str[2], font=font, fill=fontColor3)
    draw.text((75,4), rand_str[3], font=font, fill=fontColor4)
    # 9，用完画笔，释放画笔
    del draw
    # 10，存入session，用于做进一步验证
    request.session['verifyCode']=rand_str
    # 11，内存文件操作
    buf = BytesIO()
    # 12，将图片保存在内存中，文件类型为png
    im.save(buf,'png')
    # 13，将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(),'image/png')


#商品模板管理
def item_template(request):
    page_name = '商品模板管理'
    return render(request,'online/item_template.html',{'page_name':page_name})

# 商品分类管理
def item_type(request):
    page_name = '商品分类管理'
    return render(request,'online/item_type.html',{'page_name':page_name})



