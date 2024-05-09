from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import redirect
import datetime

from .models import *



############################## TOP PAGE ##############################
# def homepage(request):
#     template = loader.get_template('pages/top/index.html')

#     try:
#         customer_voices = CustomerVoice.objects.all()
#         canonical_url = "https://www.careerxrosspoint.com"
#         return render(request,'pages/top/index.html',{"customer_voices": customer_voices,'canonical_url': canonical_url})
#     except Exception as error:
#         print(str(error))

#     return HttpResponse(template.render())       

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