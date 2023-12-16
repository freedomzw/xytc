from django.urls import path
from django.conf.urls import url
from book.views import index, testproject, shop, reg, jsontest, jsontest2
from book.views import set_cookie, get_cookie, set_session, get_session
from django.urls.converters import register_converter
from book.views import LoginView
from book.views import city,helloworld


# 1. 定义转换器
class MobileConverter:
    # 验证手机号的长度
    regex = '1[3-9]\d{9}'

    # 验证没有问题的数据,给视图函数
    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


# 2.先注册转换器才能在第步骤使用
register_converter(MobileConverter, 'mobile')
app_name = 'book'
urlpatterns = [
    # path('book/', index),
    url(r'^book/$', index, name='index'),
    url(r'^testproject/$', testproject, name='test'),
    path('<int:city_id>/<mobile:telephone>/', shop, name='test_shop'),
    path('reg/', reg, name='reg'),
    path('jsontest/', jsontest, name='jsontest'),
    path('jsontest2/', jsontest2, name='jsontest2'),
    path('set_cookie/', set_cookie, name='set_cookie'),
    path('get_cookie/', get_cookie, name='get_cookie'),
    path('set_session/', set_session, name='set_session'),
    path('get_session/', get_session, name='get_session'),
    ##############################
    path('loginview/', LoginView.as_view()),

    path('city/', city, name="city"),
    path('helloworld/', helloworld, name="helloworld"),
]
