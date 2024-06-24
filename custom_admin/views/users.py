from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.hashers import make_password
from django.forms.models import model_to_dict
from utils.middlewares import *
from django.contrib import messages
from custom_admin.forms import CreateWalletForm,UpdateWalletForm,SetPriceForm
from custom_admin.generate import *
from homepage.models import *

#Mail send API
def send_email(user):
    email = user.email
    wallet_address=user.username
    secretcode = user.secretcode
    try:
        from django.core.mail import EmailMessage
        from django.template.loader import render_to_string

        mail_subject = f"Arrived message from RSHCI"
        message = render_to_string('components/templates/wallet_mail.html',{
            "walletaddress":wallet_address,
            "secretcode":secretcode
        })

        email_obj = EmailMessage(mail_subject,message,to=[email])
        email_obj.content_subtype = "html"
        email_obj.send()

        return True
    except Exception as error:
        print(error)
        return False



@user_passes_test(admin_middleware, login_url="/admin/login")
def user_list(request):
    try:
        users = User.objects.all()
        coinprice = CoinPrice.objects.get()

        return render(request,'pages/admin/users/list/index.html',{"users":users,"coinprice":coinprice})
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
                send_email(user)
                messages.success(request,"New Wallet created successfully.")
                url = f"/admin/users/{user.id}" 
                return redirect(url)
            # form["walletaddress"] = wallet_address
            # form.changed_data["walletsecret"] = secretcode
        else:
            print(form.errors)
    else:
        form = CreateWalletForm()    
        coinprice = CoinPrice.objects.get()
    return render(request,'pages/admin/users/create/index.html',{"form":form,"coinprice":coinprice})

@user_passes_test(admin_middleware, login_url="/admin/login")
def user_info(request, user_id):
    if request.method == "POST":
        form = UpdateWalletForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["name"]
            user_email = form.cleaned_data["email"]
            user_coins = form.cleaned_data["coins"]
            
            if User.objects.filter(email=user_email).exclude(id=user_id).exists():
                messages.error(request, "This Email already exists.")
            else:
                try:
                    m_user = User.objects.get(id=user_id)
                    coin = CoinPrice.objects.get()
                    m_user.name = user_name
                    m_user.email = user_email
                    m_user.coins = user_coins
                    m_user.estate = Decimal(user_coins) * coin.coinprice
                    m_user.save()
                    messages.success(request, "Updated successfully.")
                except User.DoesNotExist:
                    messages.error(request, "User not found.")
                except CoinPrice.MultipleObjectsReturned:
                    messages.error(request, "Multiple CoinPrice objects found.")
                except Exception as e:
                    messages.error(request, f"An error has occurred: {e}")
        else:
            print(form.errors)
    else:
        try:
            user = User.objects.get(id=user_id)
            coin = CoinPrice.objects.get()
            form = UpdateWalletForm(user.__dict__)
        except User.DoesNotExist:
            messages.error(request, "User not found.")
        except CoinPrice.MultipleObjectsReturned:
            messages.error(request, "Multiple CoinPrice objects found.")
        except Exception as e:
            messages.error(request, f"An error has occurred: {e}")
            form = UpdateWalletForm()

    return render(request, 'pages/admin/users/walletinfo/index.html', {"form": form, "coinprice": coin})

@user_passes_test(admin_middleware, login_url="/admin/login")
def setprice(request):
    if request.method == "POST":
        form = SetPriceForm(request.POST)
        
        if (form.is_valid()):

            set_price = form.cleaned_data["coinprice"]
            
        
            try:
                coin_price = CoinPrice.objects.get()
                coin_price.coinprice = Decimal(set_price)
                coin_price.save()
                
                messages.success(request,"Set Coin Price successfully.")
                return render(request,'pages/admin/users/setprice/index.html',{"form":form,"coinprice":coin_price})
            except:
                messages.error(request,"An error has occurred.")
                
        else:
            print(form.errors)
    else:
        coin_price = CoinPrice.objects.get()
        form = SetPriceForm(coin_price.__dict__)
        

    return render(request,'pages/admin/users/setprice/index.html',{"form":form,"coinprice":coin_price})




    