from django.db import DatabaseError
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseForbidden, HttpResponse
import re

from users.models import User


# Create your views here.

class RegisterView(View):
    """用户注册"""

    def get(self, request):
        """提供用户注册的页面"""
        return render(request, 'register.html')

    def post(self, request):
        """实现用户注册业务逻辑"""

        # 接收参数：表单参数

        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        mobile = request.POST.get('mobile')
        allow = request.POST.get('allow')

        # 判断参数是否齐全 all()回去校验列表中的元素是否为空，只要有一个为空，返回false
        if not all([username, password, password2, mobile, allow]):
            return HttpResponseForbidden('缺少必传的参数！！！')  # HttpResponseForbidden 403
        # 判断用户名是否是5-20个字符
        if not re.match(r'^[a-zA-Z0-9]{5,20}$', username):
            return HttpResponseForbidden('请输入用户名5-20个字符')
        # 判断密码是否是8-20个字符
        if not re.match(r'^[a-zA-Z0-9]{8,20}$', password):
            return HttpResponseForbidden('请输入密码8-20个字符')
        # 判断两次密码是否一致
        if password != password2:
            return HttpResponseForbidden('两次输入的密码不一致')
        # 请输入正确的手机号
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return HttpResponseForbidden('请输入正确的手机号')
        # 判断是否勾选用户协议
        if allow != 'on':
            return HttpResponseForbidden('请勾选用户协议')

        # 保存业务数据:是注册的核心代码
        try:
            User.objects.create_user(username=username, password=password, mobile=mobile)
        except DatabaseError:
            return render(request, 'register.html', {'register_msg': '注册失败'})

        return HttpResponse('注册成功,重定向到首页')


