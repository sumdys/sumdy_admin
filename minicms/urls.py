from django.conf.urls import url
from django.contrib import admin
# from learn import views as learn_views
from online import views as online_views
from backstage import views as backstage_views
from items import views as items_views
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
    url(r'^item_template/$',items_views.item_template),
    url(r'^item_type/$',items_views.item_type),
    url(r'^items/type_add/$',items_views.item_type_add),
    # url(r'^loadImages/$',learn_views.loadImage),
    # 后台系统设置
    url(r'^backstage_menu/$',backstage_views.backstage_menu),
    url(r'^backstage_menu_add/$',backstage_views.backstage_menu_add),
    url(r'^backstage_menu_info/(\d+)',backstage_views.backstage_menu_info),
    url(r'^backstage_role/$',backstage_views.backstage_role),
    url(r'^admin/', admin.site.urls),
]
