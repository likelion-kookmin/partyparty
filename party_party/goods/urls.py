from django.contrib import admin
from django.urls.conf import include
from .views import *
from django.urls import path

urlpatterns = [
    path('goods_detail/', goods_detail, name = "detail"),
    path('write_semigoods/', semi_goods, name = "write_semigoods"),
    path('write_goods/', goods, name = "write_goods"),
    path('write_choices/',write_choices,name="write_choices"),
<<<<<<< Updated upstream
]
=======
    path('mypage/', mypage, name='mypage'),
    path('myfavp/',myfavp,name='myfavp'),
    path('myfavw/',myfavw,name='myfavw'),
    path('myinfo/',myinfo,name='myinfo'),
    path('mypartiform/',mypartiform,name='mypartiform'),
    path('mytag/',mytag,name='mytag'),
    path('mywriting/',mywriting,name='mywriting'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> Stashed changes
