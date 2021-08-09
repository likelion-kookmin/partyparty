from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField

ITEM_CHOICES= {
      ('2D','2D'), #오른쪽에 있는 것이 화면에 보인다.
      ('people', '실존인물'),
      ('character', '캐릭터'),
      ('etc','그외')
  }

# Create your models here.
class Goods(models.Model) :
    
    product = models.CharField(max_length = 20) #상품명
    product_image = models.ImageField(blank = True) #제품 대표이미지
    # writer = models.ForeignKey(User, on_delete = CASCADE, related_name = "regist") #작성자
    price = models.IntegerField(null = True, blank = True, default = '') #가격
    #count = models.IntegerField() #재고
    item = models.CharField(max_length=80, choices=ITEM_CHOICES)  #상품 분류
    #end_date=models.DateField(db_column='End Date') #마감일
    #term_needs = models.DateField() #수요조사폼 기간
    #term_deposit = models.IntegerField() #입금폼 기간
    #information_needs = models.CharField(max_length=500) #수요조사폼 info
    #information_deposit = models.CharField(max_length=500) #입금폼 info
    #account_deposit = models.CharField(max_length= 50) #입금계좌
    #count_needs = models.IntegerField() #수요조사시 구매할 개수
    #count_deposit = models.IntegerField() #입금시 구매할 개수

    #howto_delivery = models.CharField(max_length=10) #배송방법
    #location1 = models.CharField(max_length=20) #주소
    #location2 = models.CharField(max_length=20) #상세주소
    #zip_code = IntegerField() #우편번호

class SemiGoods(models.Model):

    product = models.CharField(max_length = 20)
    product_image = models.ImageField()
    writer = models.ForeignKey(User, on_delete = CASCADE, related_name = "semiregist")
    semi_price = models.IntegerField()
    semi_count = models.IntegerField()
    item = models.CharField(max_length=80, choices=ITEM_CHOICES)

    email=models.EmailField(null=True,max_length = 200)
    twitter=models.CharField(max_length=20)
    information_needs = models.CharField(max_length=500)
    



