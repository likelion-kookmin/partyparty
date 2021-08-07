from django.shortcuts import render
from .models import Goods, SemiGoods
# Create your views here.


def myinfo(request):
    return render(request,'mypage.html')