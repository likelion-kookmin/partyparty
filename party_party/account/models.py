from django.db import models
from django.contrib.auth.models import AbstractUser

ITEM_CHOICES= {
    ('선택안함','선택안함'),
      ('2D','2D'), #오른쪽에 있는 것이 화면에 보인다.
      ('people', '실존인물'),
      ('character', '캐릭터'),
      ('etc','그외')
  }


class UserModel(AbstractUser):
    name = models.CharField(max_length=100,default='')
    nickname = models.CharField(max_length=100,default = '')
    phone_num = models.CharField(max_length=50,default = '')
    email = models.EmailField(null=True, max_length = 200)
    twitter = models.CharField(max_length=20,default = '')
    profile_img = models.ImageField(default ="./static/기본이미지.jpg",blank=True, null=True, upload_to ="accounts/")
    item = models.CharField(max_length=80, choices=ITEM_CHOICES,null=True, default='선택안함')
