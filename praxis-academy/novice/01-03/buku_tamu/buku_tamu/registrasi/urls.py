from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.regist, name='registrasi'),
    path('info', views.info, name='info'),
]