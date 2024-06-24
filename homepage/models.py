from django.contrib.auth.models import AbstractUser as BaseUser
from django.db import models
from decimal import Decimal


class User(BaseUser):
    name = models.CharField(max_length=100, default="")
    secretcode = models.CharField(max_length=100,default="")
    coins = models.DecimalField(decimal_places=2,max_digits=10,default=0)
    estate = models.DecimalField(decimal_places=2,max_digits=10,default=0)
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)



class Email(models.Model):

    when = models.DateTimeField(null=False, auto_now_add=True)
    to = models.EmailField(null=False, blank=False,)
    subject = models.CharField(null=False, max_length=128,)
    body = models.TextField(null=False, max_length=1024,)
    ok = models.BooleanField(null=False, default=True,)
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emails"    


class CoinPrice(models.Model):
    coinprice = models.DecimalField(max_digits=10, decimal_places=2,default=5.6)

    class Meta:
        verbose_name = "Coin Price"
        verbose_name_plural = "Coin Price"

