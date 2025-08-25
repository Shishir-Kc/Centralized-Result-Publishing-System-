from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CustomUser,School


def home(request):
   return HttpResponse ("hello")

def user_login(request):
    if request.method == "POST":
        print("nigggga")
        print("email - > ", request.POST.get("user_email"))
        print("Password - > ", request.POST.get("user_password"))
        return render(request,'accounts/login.html')   
    

    else:


     return render(request,'accounts/login.html')


def user_register(request):
    if request.method == "POST":
       school_name = request.POST.get('school_name')
       address = request.POST.get('address')
       contact = request.POST.get('contact')
       email = request.POST.get('email')
       user_name = request.POST.get('admin_username')
       user_password = request.POST.get('admin_pass')
       print(school_name,
             address,
             contact,
             email,
             user_name,
             user_password,
             )
       school_obj = School.objects.create(name = school_name)

       reg_obj = CustomUser.objects.create(username=user_name,password=user_password,email=email,contact=contact,account_status =CustomUser.is_valid.PENDING,registered_school =school_obj) 
       return HttpResponse ("yolooo ")
    else:
       

     return render(request,'accounts/register.html')