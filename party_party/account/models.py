from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserModel(AbstractUser):
    
    nickname = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=50)
    profile_img = models.ImageField(default ="../static/account_standard.jpg",blank=True, null=True, upload_to ="accounts/")
    