from django.shortcuts import render
from .models import Goods, SemiGoods

def goods_detail(request) :
    goods = Goods.object.all()
    return render(request, 'goods_detail.html')


def write_choices(request):
    return render(request, 'write_choices.html')

def semigoods_choices(request):
    return render(request,"semigoods_choices.html")
def semi_goods(request) : #수요조사폼이 글작성
    semigoods=SemiGoods.object.all()
    return render(request, 'write_semigoods.html')


def goods(request): #입금폼 작성
    goods = Goods.object.all()
    return render(request, 'write_goods.html')

def create_semi(request):
    if(request.method == 'POST'):
        new_idea.product = request.POST['title']
        new_idea.writer = request.user
        new_idea.pud_date = timezone.now()

        new_idea.email=request.POST['email']
        new_idea.twitter=request.POST['twitter']
        new_idea.item = request.POST['item']

        if not request.FILES:
            new_idea.image = ""
            new_idea.save()

        else:
            new_idea.image = request.FILES['image']
            new_idea.save()

    return redirect('detail', new_idea.id)




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


