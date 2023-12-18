from django.urls import re_path
from users.views import RegisterView, UsernameCountView, PhoneCountView

urlpatterns = [

    # 首页路由
    re_path(r'^register/$', RegisterView.as_view(), name='register'),

    # url(r'^register/$', views.RegisterView.as_view(), name='register'), 语法同re_path
    re_path(r'^usernames/(?P<username>[a-zA-Z0-9]{5,20})/count/$', UsernameCountView.as_view()),

    # 手机号路由
    re_path(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$', PhoneCountView.as_view())
]
