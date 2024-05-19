from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from custom_admin.forms import AdminLoginForm



def admin_login(request):
   
    
    # if request.user.is_authenticated:
    #     return redirect("/")
    
    if request.method == "POST":
        form = AdminLoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            if user is not None:
                # A backend authenticated the credentials

                if user.is_superuser:
                    login(request, user)
                    return redirect("/admin/dashboard")
                else:
                    logout(request)
                    form.non_field_errors = "This user does not have permissions."
            else:
                # No backend authenticated the credentials
                form.non_field_errors = "Please enter the correct username and password for your staff account. Both fields are case sensitive."
        else:
            print(form.errors)      

    else:
        form = AdminLoginForm()

    
    return render(request, "pages/admin/login/index.html", {"form": form})