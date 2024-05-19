from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from utils.middlewares import *
from django.contrib import messages

@user_passes_test(admin_middleware, login_url="/admin/login")
def index(request):
    try:

        return render(request,'pages/admin/dashboard/index.html',{})
    except:
        messages.warning(request,'Invalid request parameters.')

    return render(request,'pages/admin/dashboard/index.html')


