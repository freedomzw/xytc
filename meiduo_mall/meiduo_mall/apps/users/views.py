from django.contrib.auth import login
from django.db import DatabaseError
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.http import HttpResponseForbidden, HttpResponse, JsonResponse
from meiduo_mall.utils.response_code import RETCODE

import re

from users.models import User


class UsernameCountView(View):

    def get(self, request, username):
        """

        :param request:
        :param username:  用户名
        :return: JSON

        """

        # 实现主体业务逻辑：使用username查询对应的记录的条数
        count = User.objects.filter(
            username=username
        ).count()

        # 响应结果
        return JsonResponse({'code': 0, 'errmsg': 'RETCODE.ok', 'count': count})


class PhoneCountView(View):

    def get(self, request,mobile):
        """
        用于判断手机号是否有重复
        :param request:
        :param mobile:  手机号
        :return: JSON
        """

        count = User.objects.filter(
            mobile=mobile
        ).count()

        return JsonResponse({'code': 0, 'errmsg': 'RETCODE.ok', 'count': count})


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

        # return render(request, 'register.html', {'register_errmsg': '注册失败'})

        # 保存业务数据:是注册的核心代码
        try:
            user = User.objects.create_user(username=username, password=password, mobile=mobile)
        except DatabaseError:
            return render(request, 'register.html', {'register_msg': '注册失败'})

        # return HttpResponse('注册成功,重定向到首页')

        login(request, user, backend=None)

        return redirect(reverse('contents:index'))
