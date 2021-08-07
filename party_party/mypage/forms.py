from django import forms
from .models import Goods, SemiGoods,UserModel 

class myinfoform(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = (
            'nickname'
        )