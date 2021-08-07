from django.contrib import admin
from django.urls.conf import include
from .views import *
from django.urls import path

urlpatterns = [
    path('mypage/', mypage, name = "mypage"),
    path('myinfo/', myinfo, name = "myinfo"),
    path('myform/', myform, name = "myform"),
    path('myparti/',myparti,name="myparti"),
    path('myfavwriter/', myfavwriter, name = "myfavwriter"),
    path('myfavwriting/', myfavwriting, name = "myfavwriting"),
    path('mytag/', mytag, name = "mytag"),
]