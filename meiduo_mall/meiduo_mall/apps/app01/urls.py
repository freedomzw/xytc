from django.urls import path
from app01.views import index

# 声明namespace 为app01
app_name = 'app01'

urlpatterns = [
    path('index/', index, name='index'),
]
