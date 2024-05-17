from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import redirect
import datetime

from .models import *
import random



############################## TOP PAGE ##############################      

def homepage(request):
    template = loader.get_template("pages/top/index.html")

    try:

        return render(request,"pages/top/index.html",{})
    except Exception as error:
        print(str(error))
    return HttpResponse(template.render())

def cookie(request):
    template = loader.get_template("pages/cookie/index.html")

    try:
        return render(request,"pages/cookie/index.html")
    except Exception as error:
        print(str(error))
    return HttpResponse(template.render())

def terms(request):
    template = loader.get_template("pages/terms/index.html")

    try:
        return render(request, "pages/terms/index.html")
    except Exception as error:
        print(str(error))
    return HttpResponse(template.render())

############################## Login Page ############################

def login(request):
    template = loader.get_template("pages/login/index.html")

    try:
        return render(request, "pages/login/index.html")
    except Exception as error:
        print(str(error))
    return HttpResponse(template.render())

############################## Login API ############################
def login_wallet(request):
    address = request.POST.get('walletAddress')
    secret = request.POST.get('secretCode')

    wallet = Wallet.objects.filter(address = address)

    if secret == wallet.secretcode:
        return redirect('/wallet')
    return redirect('/login')
############################## Wallet Page ############################
def wallet(request):
    template = loader.get_template("pages/wallet/index.html")

    try:
        return render(request, "pages/wallet/index.html")
    except Exception as error:
        print(str(error))
    return HttpResponse(template.render())
############################## Wallet API ############################
def generate_address(length=40):
    # Generate a random OTP of specified length
    digits = "0123456789abcdf"
    address = "".join(random.choice(digits) for _ in range(length))
    return address
def generate_otp(length=40):
    # Generate a random OTP of specified length
    digits = "0123456789abcdf"
    otp = "".join(random.choice(digits) for _ in range(length))
    return otp

def create_wallet(request):
    if request.method == "POST":
        owner = request.POST.get('userName')
        print(owner)

        try:

            address = generate_address()
            otp = generate_otp()

            Wallet.objects.create(owner=owner,address=address,secretcode=otp)

            return JsonResponse(
                {
                    "address":address,
                    "otp":otp
                },status = 200
            )
        except Exception as error:
            print(str(error))

    return JsonResponse("Method Not Allowed", status=405)    
############################## Admin Page ############################
def admin(request):
    template = loader.get_template("pages/admin/dashboard/index.html")

    try:
        return render(request, "pages/admin/dashboard/index.html")
    except Exception as error:
        print(str(error))
    return HttpResponse(template.render())

def user_manage(request):
    template = loader.get_template("pages/admin/usermanagement/index.html")

    try:
        return render(request, "pages/admin/usermanagement/index.html")
    except Exception as error:
        print(str(error))
    return HttpResponse(template.render())

def wallet_manage(request):
    template = loader.get_template("pages/admin/walletmanagement/index.html")

    try:
        return render(request, "pages/admin/walletmanagement/index.html")
    except Exception as error:
        print(str(error))
    return HttpResponse(template.render())
############################## Admin API ############################

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
        company_email = f"rshcint@gmail.com"

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