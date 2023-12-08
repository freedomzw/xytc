from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers

# Create your views here.

from book.models import BookInfo
import json


def index(request):
    # books = BookInfo.objects.all()
    data = serializers.serialize("json", BookInfo.objects.all())
    print(data)
    return HttpResponse(json.dumps(data))


def testproject(request):
    return HttpResponse('测试项目逻辑')


def shop(request, city_id, shop_id):
    print(city_id, shop_id)
    query_params = request.GET
    print(query_params)  # http://0.0.0.0/11/1111/?search=%22%E9%A3%9E%E6%9C%BA%22
    key = query_params.get("search")
    print(key)
    return HttpResponse('宫保鸡丁盖饭!!!')


def reg(request):
    '''传送form—data数据'''
    data_form = request.POST
    print(data_form['username'])
    print(data_form['password'])
    return HttpResponse("ok")

def jsontest(request):
    '''json的数据传输'''
    request.POST
    return HttpResponse("json")