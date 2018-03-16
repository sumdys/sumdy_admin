from django.conf.urls import url,include
from django.contrib import admin
from online import views as online_views
<<<<<<< HEAD
=======
from backstage import views as backstage_views
from items import views as items_views
>>>>>>> master
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
<<<<<<< HEAD
    # 商品
    url(r'^items/',include('items.urls')),
=======
    url(r'^item_template/$',items_views.item_template),
    url(r'^item_type/$',items_views.item_type),
    url(r'^items/type_add/$',items_views.item_type_add),
>>>>>>> master
    # url(r'^loadImages/$',learn_views.loadImage),
    # 后台系统设置
    url(r'^admin/', admin.site.urls),
    url(r'^backstage/',include('backstage.urls')),
]
