from django.urls import path, include, re_path
from . import views
from django.conf.urls import url

urlpatterns = [

    #首页路由
    re_path(r'^register/$', views.RegisterView.as_view(), name='register'),
    # url(r'^register/$', views.RegisterView.as_view(), name='register'), 语法同re_path
    re_path(r'^usernames/(?P<username>[a-zA-Z0-9]{5,20})/count/$', views.UsernameCountView.as_view()),

    # 手机号路由
    re_path(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$', views.PhoneCountView.as_view())
]
