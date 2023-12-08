from django.urls import path
from app02.views import index

# 声明namespace 为app02
app_name = 'app02'

urlpatterns = [
    path('index/', index, name='index'),
]
