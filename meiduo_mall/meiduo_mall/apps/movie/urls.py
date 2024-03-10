from django.urls import re_path, path
from rest_framework.urlpatterns import format_suffix_patterns

from movie import views

app_name = 'movie'
urlpatterns = [
    path('list/', views.movie_list, name='list'),
    path('test/', views.book_test, name='test'),
    re_path(r'^(\d+)/(\d+)/$', views.detail, name='detail'),
    path('one_test/', views.find_one_id, name='one'),
    path('one_frist/', views.one_frist, name='frist'),
    path('list_find/', views.list_find, name='list_find'),
    path('reverse_index/',views.reverse_index,name='index'),
    path('index/',views.index),
    path('header_test/',views.header_test,name='header'),
    path('set_cookie/',views.set_cookie,name='set_cookie'),
    path('get_cookie/',views.get_cookie,name='get_cookie'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
