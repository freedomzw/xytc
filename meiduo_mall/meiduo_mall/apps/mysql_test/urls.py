from django.urls import path, re_path
from django.conf.urls import url
from mysql_test.views import query_by_id
from mysql_test.views import index
from mysql_test.views import test
from mysql_test.views import special_case_2003, year_archive, month_archive, article_detail
from mysql_test.views import index2
from mysql_test.views import index3

app_name = 'mysql_test'
urlpatterns = [

    # 根据id进行查询
    re_path(r'^query_by_id/$', query_by_id, name='query_by_id'),
    path('index/', index, name='index'),
    url(r'^test/$', test, name='test'),

    ####################位置参数####################

    url(r'^(\w?)/(\w*)/(\w+)/$', index2, name='index2'),

    ####################关键字参数####################

    url(r'^(?P<value1>\d+)/(?P<value2>\d+)/$', index3,name='index3'),
    # url(r'^articles/2003/$', special_case_2003),
    # url(r'^articles/(?P<year>[0-9]{4})/$', year_archive),
    # url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', month_archive),
    # url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', article_detail),

]
