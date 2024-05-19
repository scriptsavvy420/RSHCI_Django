from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.hashers import make_password
from django.forms.models import model_to_dict
from utils.middlewares import *
from django.contrib import messages
from custom_admin.forms import CreateWalletForm,UpdateWalletForm
from custom_admin.generate import *
from homepage.models import *



@user_passes_test(admin_middleware, login_url="/admin/login")
def user_list(request):
    try:
        users = User.objects.all()

        return render(request,'pages/admin/users/list/index.html',{"users":users})
    except:
        messages.warning(request,'Invalid request parameters.')

    return render(request,'pages/admin/users/list/index.html')

@user_passes_test(admin_middleware, login_url="/admin/login")
def user_create(request):
    if request.method =="POST":
        form = CreateWalletForm(request.POST)

        if form.is_valid():

            user_name = form.cleaned_data["name"]
            user_email = form.cleaned_data["email"]

            validate_email = User.objects.filter(email=user_email)

            if validate_email.exists():
                form.add_error(None, "This email already exists. Retry with another email.")
            else:
                wallet_address = generate_address()
                secretcode = generate_secretcode()
                password = make_password(secretcode)
                user = User.objects.create(username=wallet_address,password=password,name=user_name,email=user_email,secretcode=secretcode)

                messages.success(request,"New Wallet created successfully.")
                url = f"/admin/users/{user.id}" 
                return redirect(url)
            # form["walletaddress"] = wallet_address
            # form.changed_data["walletsecret"] = secretcode
        else:
            print(form.errors)
    else:
        form = CreateWalletForm()    

    return render(request,'pages/admin/users/create/index.html',{"form":form})

@user_passes_test(admin_middleware, login_url="/admin/login")
def user_info(request, user_id):
    
    
    if request.method == "POST":
        form = UpdateWalletForm(request.POST)
        if (form.is_valid()):

            user_name = form.cleaned_data["name"]
            user_email = form.cleaned_data["email"]
            user_coins = form.cleaned_data["coins"]
            
            if User.objects.filter(email = user_email).exclude(id=user_id).exists():
                messages.error(request,"This Email already exists.")
            else:
                try:
                    m_user = User.objects.get(id=user_id)
                    m_user.name = user_name
                    m_user.email = user_email
                    m_user.coins = user_coins
                    m_user.save()
                    messages.success(request,"Updated successfully.")
                except:
                    messages.error(request,"An error has occurred.")
                
        else:
            print(form.errors)
    else:
        user = User.objects.get(id=user_id)
        form = UpdateWalletForm(user.__dict__)
        

    return render(request,'pages/admin/users/walletinfo/index.html',{"form":form})





    