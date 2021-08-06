from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField

# Create your models here.
class Goods(models.Model) :
    product = models.CharField(max_length = 20)
    product_image = models.ImageField()
    writer = models.ForeignKey(User, on_delete = CASCADE, related_name = "regist")
    price = models.IntegerField()
    count = models.IntegerField()
    
    term_needs = models.DateField()
    term_deposit = models.IntegerField()
    information_needs = models.CharField(max_length=500)
    information_deposit = models.CharField(max_length=500)
    account_deposit = models.CharField(max_length= 50)
    count_needs = models.IntegerField()
    count_deposit = models.IntegerField()

    howto_delivery = models.CharField(max_length=10)
    location1 = models.CharField(max_length=20)
    location2 = models.CharField(max_length=20)
    zip_code = IntegerField()




