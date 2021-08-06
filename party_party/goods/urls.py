from django.contrib import admin
from django.urls.conf import include
from .views import *
from django.urls import path

urlpatterns = [
    path('goods_detail/<str:goods_id>', goods_detail, name = "detail"),
]