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
