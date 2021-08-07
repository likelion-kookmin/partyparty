from django.contrib import admin
from django.urls import path, include, re_path
from mypage import views
from django.conf import settings
from django.conf.urls.static import static


path('mypage/', views.mypage, name='mypage'),
path('myfavp/',views.myfavp,name='myfavp'),
path('myfavw/',views.myfavw,name='myfavw'),
path('myinfo/',views.myinfo,name='myinfo'),
path('mypartiform/',views.mypartiform,name='mypartiform'),
path('mytag/',views.mytag,name='mytag'),
path('mywriting/',views.mywriting,name='mywriting'),