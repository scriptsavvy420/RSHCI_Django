from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import user_passes_test
from utils.middlewares import *
from django.template import loader
from django.shortcuts import redirect
from homepage.forms import ClientLoginForm,ClientWalletForm
from .models import *
from django.contrib import messages
import datetime




############################## TOP PAGE ##############################      

def homepage(request):
    template = loader.get_template("pages/top/index.html")

    try:
        coinprice = CoinPrice.objects.get()

        return render(request,"pages/top/index.html",{"coinprice":coinprice})
    except Exception as error:
        print(str(error))
    return HttpResponse(template.render())

def cookie(request):
    template = loader.get_template("pages/cookie/index.html")
    
    try:
        coinprice = CoinPrice.objects.get()
        return render(request,"pages/cookie/index.html",{"coinprice":coinprice})
    except Exception as error:
        print(str(error))
    return HttpResponse(template.render())

def terms(request):
    template = loader.get_template("pages/terms/index.html")
    

    try:
        coinprice = CoinPrice.objects.get()
        return render(request, "pages/terms/index.html",{"coinprice":coinprice})
    except Exception as error:
        print(str(error))
    return HttpResponse(template.render())

def privacy(request):
    template = loader.get_template("pages/privacy/index.html")
    

    try:
        coinprice = CoinPrice.objects.get()
        return render(request, "pages/privacy/index.html",{"coinprice":coinprice})
    except Exception as error:
        print(str(error))
    return HttpResponse(template.render())

############################## Login Page ############################

def client_login(request):
    

    if request.method == "POST":
        form = ClientLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username,password=password)
            if user is not None:
                m_user = User.objects.get(username=username)
                login(request,user)
                url = f"/wallet/{m_user.id}"
                return redirect(url)
            else:
                logout(request)
                form.non_field_errors = "Login failed.Make sure your wallet address and password are correct."

        else:
            print(form.errors)
    else:
        form = ClientLoginForm()
        coinprice = CoinPrice.objects.get()

    return render(request,"pages/login/index.html",{"form":form,"coinprice":coinprice})       
        


############################## Wallet Page ############################
@user_passes_test(user_middleware, login_url="/login")
def wallet(request,user_id):
    user = User.objects.get(id=user_id)
    coin = CoinPrice.objects.get()
    coinprice = coin.coinprice
    if request.method == "POST":
        form = ClientWalletForm(request.POST)
        if form.is_valid():
            recieve_username = form.cleaned_data["recieve_address"]
            send_coins = int(form.cleaned_data["send_coins"])
            send_user = User.objects.get(id=user_id)
            current_coins = int(send_user.coins)
            recieve_user = User.objects.get(username=recieve_username)
            if current_coins >= send_coins :
                send_user.coins -= send_coins
                send_user.estate = Decimal(send_user.coins)*coinprice
                send_user.save()
                recieve_user.coins+=send_coins
                recieve_user.estate = Decimal(recieve_user.coins)*coinprice
                recieve_user.save()
                messages.success(request,"The transaction was successful.")
                form = ClientWalletForm(send_user.__dict__)

                return render(request,'pages/wallet/index.html',{"user":send_user,"form":form,"coinprice":coinprice})
            else:
                messages.warning(request,"There are currently not enough coins in your possession.Please double check the quantity you wish to send.")
            #reciever wallet address

        else:
            print(form.errors)
    else:
        
        form = ClientWalletForm(user.__dict__)
    return render(request,'pages/wallet/index.html',{"user":user,"form":form,"coinprice":coin}) 

############################## MAIL API ##############################
def send_mail(request):

    if request.method == 'POST':

        name = request.POST.get('contact-name')
        email = request.POST.get('contact-email')
        phone = request.POST.get('contact-phone')
        disires = request.POST.get('contact-disires')
        amount = request.POST.get('contact-investAmount')
        periods = request.POST.get('contact-investPeriods')

        description = request.POST.get('contact-text')
        company_email = f"yoshidadaisuke0420@gmail.com"

        try:
            from django.core.mail import EmailMessage
            from django.template.loader import render_to_string

            
            mail_subject = f"Arrived message from {name}"
            message = render_to_string("components/templates/contact_mail.html", {
                "name": name,
                "email": email,
                "phone": phone,
                "disires":disires,
                "amount":amount,
                "periods":periods,
                "description": description
            })

            email_obj = EmailMessage(
                mail_subject, message, to=[company_email]
            )
            email_obj.content_subtype = "html"
            email_obj.send()

            return JsonResponse({
                "success": True
            }, status=200)
            
        except Exception as error:
            print(error)
            return JsonResponse(str(error), status=400)

    return JsonResponse("Method Not Allowed", status=405)