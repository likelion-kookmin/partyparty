from django.shortcuts import render
from .models import Goods

def goods_detail(request) :
    goods = Goods.object.all()
    return render(request, 'goods_detail.html')
