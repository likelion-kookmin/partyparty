from django.shortcuts import render
from .models import Goods

def goods_detail(request) :
    #goods = Goods.object.all()
    return render(request, 'goods_detail.html')


def write_choices(request):
    return render(request, 'write_choices.html')

def semi_goods(request) : #수요조사폼이 글작성
    semigoods=SemiGoods.object.all()
    return render(request, 'write_semigoods.html')


def goods(request): #입금폼 작성
    goods = Goods.object.all()
    return render(request, 'write_goods.html')
    