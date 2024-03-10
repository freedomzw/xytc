from django.shortcuts import redirect
from django.urls import reverse
from django.db.models import F
from django.http import JsonResponse, HttpResponseGone, HttpResponse

from book.models import BookInfo
from meiduo_mall.utils.serializer import MovieListSerializer


def movie_list(request):
    """查询全部的数据"""
    # # 获取数据
    # movies = BookInfo.objects.all().values_list()
    # # data 获取数据库中的全部的数据
    # data = list(movies)
    # # data2 数据获取自定义的全部的数据
    # data2 = {
    #     'movie_name':'碟中谍',
    #     'rate':7.8
    # }
    # # safe不进行转义False
    # return JsonResponse(data2, safe=False)

    movies = BookInfo.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return JsonResponse(serializer.data, safe=False)


def book_test(request):
    """测试一条json数据"""
    json_test = {'city': 'beijing', 'subject': 'python'}
    return JsonResponse(json_test)


def detail(request, a, b):
    print(request.path)
    return HttpResponse('ok')


def find_one_id(request):
    one_filter = BookInfo.objects.filter(id__exact=2).values_list()
    # print(one_filter)
    # print(1)
    data = list(one_filter)
    return JsonResponse(data, safe=False)


def one_frist(request):
    frist_one = BookInfo.objects.filter(name__contains='传').values_list()
    data = list(frist_one)
    return JsonResponse(data, safe=False)


def list_find(request):
    list__isnull = BookInfo.objects.filter(pub_date__year='2024').values_list()
    data = list(list__isnull)
    return JsonResponse(data, safe=False)


def field_two(request):
    b = BookInfo.objects.filter(readcount__gt=F('commentcount')).values_list()
    data = list(b)
    return JsonResponse(data, safe=False)


def reverse_index(request):
    path = reverse('movie:index')
    print(path)
    return redirect(path)


def index(request):
    # path = request.GET
    # k1 = request.POST.get('username')
    # k2 = request.POST.get('password')
    # k3 = request.POST.getlist('username')
    # print(path,k1,k2,k3)
    """
    json是双引号{
        "name":"itcast"
    }
    :param request:
    :return:
    """
    body = request.body
    print(body)
    print("=======")
    return HttpResponse('ok')


#######################打印头--header######################
def header_test(request):
    header = request.META
    # 打印header信息
    print(header)
    # 打印reverse信息
    path = reverse('movie:header')
    print(path)
    return HttpResponse('ok')


def set_cookie(request):
    username = request.GET.get('username')
    response = HttpResponse('set_cookie')
    response.set_cookie('username', username)
    return response


def get_cookie(request):
    # 1.服务器可以接收(查看)cookie信息
    cookie = request.COOKIES
    # cookies 就是一个字典
    username = cookie.get('username')

    # 得到用户信息就可以继续其他的业务逻辑了

    # 响应
    response = HttpResponse("ok")
    return response
