from django.shortcuts import render
from django.views import View


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

        # 保存图形验证码
        # 响应图形验证码
        # 响应结果
        pass
