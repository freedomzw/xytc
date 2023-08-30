from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.


from mysql_test.models import UserTest


def query_by_id(request):
    """
        根据id进行查询
    :param request:
    :param id: uid
    :return:
    """

    my_object = UserTest.objects.all()
    for obj in my_object:
        print(obj)

    # return HttpResponse('ok')

    return JsonResponse({'code': 0, 'errmsg': 'RETCODE.ok', 'id': obj})
