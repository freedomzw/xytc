from django.urls import path
from django.conf.urls import url
from book.views import index, testproject, shop, reg, jsontest

app_name = 'book'
urlpatterns = [
    # path('book/', index),
    url(r'^book/$', index, name='index'),
    url(r'^testproject/$', testproject, name='test'),
    path('<city_id>/<shop_id>/', shop, name='test_shop'),
    path('reg/', reg, name='reg'),
    path('jsontest/', jsontest, name='jsontest'),
]
