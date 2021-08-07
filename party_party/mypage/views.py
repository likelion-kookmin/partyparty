from .models import Goods,SemiGoods
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import myinfoform
from django.db.models import Count
from account.models import UserModel
#from account.forms import RegisterForm
from django.db import models
from django.conf import settings
from django.core.paginator import Paginator




def mypage(request):
    return render(request, 'mypage.html')


def mypartiform(request):
    return render(request, 'mypartiform.html')


def myinfo(request):
    return render(request, 'myinfo.html')


def myfavp(request):
    return render(request, 'myfavp.html')



def myfavw(request):
    return render(request, 'myfavw.html')

def mytag(request):
    return render(request, 'mytag.html')


def mywriting(request):
    return render(request, 'mywriting.html')
