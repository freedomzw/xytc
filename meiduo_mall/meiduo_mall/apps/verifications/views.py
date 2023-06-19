from django.shortcuts import render
from django.views import View
from django_redis import get_redis_connection

from verifications.libs.captcha.fonts.captcha import captcha
from django import http

# Create your views here.
class ImageCodeView(View):
    """图形验证码"""

    def get(self, request, uuid):
        """
        :param request:
        :param uuid: 通用的唯一识别码，用于唯一标识该图形验证码属于哪个用户的
        :return: image/jgp
        """
        # 接收和校验参数
        # 实现主体业务逻辑：生成、保存、响应图形验证码
        # 生成图形验证码
        text, image = captcha.generate_captcha()
        # 保存图形验证码 verify_code 这个名字是redis库的名字
        redis_conn = get_redis_connection('verify_code')
        # redis_conn.setex('key', 'expires', 'value')
        redis_conn.setex(f'{uuid}', 300, text)
        # 响应图形验证码

        # 响应结果

        return http.HttpResponse(image,content_type='image/jpg')