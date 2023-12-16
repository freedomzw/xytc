from django.http import HttpResponse, JsonResponse
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


def shop(request, city_id, telephone):
    print(city_id, telephone)
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
    # request.POST
    body_data = request.body
    body_str = body_data.decode('utf-8')  # 打印的是字符串
    print(type(body_data.decode('utf-8')))
    '''json形式的字符串可以转换成字典'''
    import json
    body_dict = json.loads(body_str)
    print(body_dict)  # 打印出来的是字典{'name': 'zhangsan', 'age': 18}
    return HttpResponse("json")


def jsontest2(request):
    friends_list = [
        {
            "name": "zhangsan",
            "age": 19
        }, {
            "name": "lisi",
            "age": 30
        }
    ]

    return JsonResponse(data=friends_list, safe=False)


def set_cookie(request):
    # 1.通过参数获取query_data
    us = request.GET.get("username")
    pw = request.GET.get("password")
    # 2.通过response设置cookie
    response = HttpResponse("Welcome!!!")
    '''cookie设置是key value'''
    response.set_cookie("us", us, expires=3600)
    response.set_cookie("pw", pw, expires=3600)
    return response


def get_cookie(request):
    us_cooke = request.COOKIES.get("us")
    pw_cooke = request.COOKIES.get("pw")
    print(us_cooke, pw_cooke)
    return HttpResponse("我要拿到cookie")


##########################################################
"""
    1、session 是保存在服务器上的，相对安全
    2、session 需要依赖于cookie，所以要先有cookie
    第一次请求的服务器的时候，服务器会设置一个sessionid的cookie信息发送给客户端
    第二次请求的时候 都会携带这个sessionid 服务器验证这个sessionid 验证没有问题会读取
    相关数据
    
"""


def set_session(request):
    """设置session的数据 session必须要依赖cookie的数据"""
    # 写入redis
    # 1.通过参数获取query_data
    us = request.GET.get("username")
    pw = request.GET.get("password")

    # 假如 我们通过模型查询 查询到了 用户的信息
    user_id = 1

    request.session['user_id'] = user_id
    request.session['username'] = us
    request.session['password'] = pw

    return HttpResponse("set_session")


def get_session(request):
    user_id = request.session.get('user_id')
    username = request.session.get('username')
    password = request.session.get('password')
    content = '{},{},{}'.format(user_id, username, password)
    return HttpResponse(content)


from django.views import View


class LoginView(View):
    """继承view """

    def get(self, request):
        return HttpResponse('get')

    def post(self, request):
        return HttpResponse('post')


from django.template import loader


def city(request):
    template = loader.get_template('zhaowei.html')
    print(template)
    context = {'city': '北京'}

    return render(request, 'zhaowei.html', context)


def helloworld(request):
    return render(request,'hello-world.html')