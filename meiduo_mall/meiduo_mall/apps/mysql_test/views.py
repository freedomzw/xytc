from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
import json
# Create your views here.


from mysql_test.models import UserTest


def query_by_id(request):
    """
        查询第一个值
    :param request:
    :param id: uid
    :return:
    """

    # my_object = UserTest.objects.all()
    # for obj in my_object:
    #     print(type(obj),obj)

    the_first_data = UserTest.objects.first()
    serializers.serialize("json")

    # return HttpResponse('ok')

    return JsonResponse({'code': 0, 'errmsg': 'RETCODE.ok', 'id': the_first_data})


def query_by_name(request):
    return HttpResponse('ok')


def index(request):
    return HttpResponse('index')


def index2(request, value1, value2, value3):
    # 构造上下文
    context = {'v1': value1, 'v2': value2, 'v3': value3}
    print(context)

    return HttpResponse('index2')


def index3(request, value1, value2):
    # 构造上下文
    context = {'v1': value1, 'v2': value2}
    print(context)
    return HttpResponse('index3')


def test(request):
    return HttpResponse('test')


def month_archive(request, year, month):
    return HttpResponse('month_archive')


def year_archive(request, year):
    return HttpResponse('year_archive')


def special_case_2003(request, month):
    return HttpResponse('special_case_2003')


def article_detail(request, year, month, day):
    return HttpResponse('article_detail')
