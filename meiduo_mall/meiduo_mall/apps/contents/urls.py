from django.urls import re_path
from . import views
from django.conf.urls import url

urlpatterns = [

    # 首页广告路由
    re_path(r'^index/$', views.IndexView.as_view(), name='index'),
    # url(r'^contents/$', views.IndexView.as_view(), name='contents'),

]
