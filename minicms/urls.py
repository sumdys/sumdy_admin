"""minicms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# from learn import views as learn_views
from online import views as online_views
from backstage import views as backstage_views
admin.autodiscover()


urlpatterns = [
    # url(r'^$',learn_views.index),
    url(r'^register/$',online_views.register,name='register'),
    # url(r'^login/$',online_views.login),
    url(r'^login/$', online_views.login),
    url(r'^index/$',online_views.index),
    url(r'^logout/$',online_views.logout),
    url(r'^verify_code/$',online_views.verify_code),
    url(r'^login_ajax_check/$',online_views.login_ajax_check),
    url(r'^item_template/$',online_views.item_template),
    url(r'^item_type/$',online_views.item_type),
    # url(r'^loadImages/$',learn_views.loadImage),
    # 后台系统设置
    url(r'^backstage_menu/$',backstage_views.backstage_menu),
    url(r'^backstage_menu_add/$',backstage_views.backstage_menu_add),
    url(r'^backstage_role/$',backstage_views.backstage_role),
    url(r'^admin/', admin.site.urls),
]
