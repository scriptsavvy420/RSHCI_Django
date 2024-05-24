from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from utils.middlewares import *
from django.contrib import messages
from homepage.models import *

@user_passes_test(admin_middleware, login_url="/admin/login")
def index(request):
    try:
        coinprice = CoinPrice.objects.get()
        return render(request,'pages/admin/dashboard/index.html',{"coinprice":coinprice})
    except:
        messages.warning(request,'Invalid request parameters.')

    return render(request,'pages/admin/dashboard/index.html')


