from django.urls import path, include, re_path
from . import views
from django.conf.urls import url

urlpatterns = [

    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    # path('register/', views.RegisterView.as_view()),
]
