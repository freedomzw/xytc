from django.urls import path, include, re_path
from . import views

urlpatterns = [

    # 根据id进行查询
    re_path(r'^query_by_id/$', views.query_by_id),

]
