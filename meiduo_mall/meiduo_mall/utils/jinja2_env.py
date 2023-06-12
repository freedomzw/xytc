# Jinja2模板引擎环境配置
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment


def jinja2_enviroment(**options):
    """jinja2环境"""
    # 创建环境对象

    env = Environment(**options)

    # 自定义语法： {{ static('静态文件相对路径') }} {{ url('路由的命名空间') }}

    env.globals.update({
        'static': staticfiles_storage.url,  # 获取静态文件的前缀
        'url': reverse,
    })
    # 返回环境对象
    return env


def jinja2_env(**kwargs):
    """
    使模板引擎可以使用{{ url('') }}和{{ static('') }}语句
    :return:
    """
    env = Environment(**kwargs)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url':  reverse
    })
    return env