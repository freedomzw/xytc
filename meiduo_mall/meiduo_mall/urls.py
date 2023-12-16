"""meiduo_mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [

    path('admin/', admin.site.urls),

    path('app01/', include('app01.urls', namespace='app01')),
    path('app02/', include('app02.urls', namespace='app02')),

    url(r'^', include('book.urls', namespace='book')),

    # mysql_test
    path('mysql/', include('mysql_test.urls', namespace='mysql_test')),

    # users 应用
    url(r'^', include(('users.urls', 'users'), namespace='users')),

    # contents 应用
    url(r'^', include(('contents.urls', 'contents'), namespace='contents')),

    # verifications
    url(r'^', include('verifications.urls')),

]

# 重定向 127.0.0.1直接跳转到Blog
from django.views.generic import RedirectView

urlpatterns += [
    path('', RedirectView.as_view(url='/register/'))
]
