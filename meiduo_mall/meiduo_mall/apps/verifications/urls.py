from django.conf.urls import url
from . import views

urlpatterns = [
    # 图形验证码
    # http://0.0.0.0/image_code/1-1-1-1/
    url(r'^image_codes/(?P<uuid>[\w-]+)/$', views.ImageCodeView.as_view())
]
