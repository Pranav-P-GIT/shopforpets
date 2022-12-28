from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import PetProduct
from django.conf import settings
from django.core.mail import send_mail




# Create your views here.
def index(request):
    data=PetProduct.objects.all
    if "pas" in request.COOKIES and "price" in request.COOKIES:
        var=request.COOKIES["pas"]
        price=request.COOKIES["price"]
        return render(request,"index.html",{"abc":var,"pro":data,"efg":price})
    else:


        return render(request,"index.html",{"pro":data})
def test(request):

    val="php"
    return render(request,"test.html",{"a":val,"b":"object oriented"})
def register(request):
    if request.method=="POST":
        username=request.POST["uname"]
        firstname=request.POST["fname"]
        lastname=request.POST["lname"]
        gmail=request.POST["mail"]
        password=request.POST["password"]
        repassword=request.POST["ppassword"]
        ucheck=User.objects.filter(username=firstname)
        echeck=User.objects.filter(email=gmail)
        if ucheck:
            msg="username is already taken"
            return render(request,"register.html",{"b":msg})
        #elif echeck:
            msge="email is already taken"
            return render(request,"register.html",{"b":msge}) 
        elif password=="" or password!=repassword:
            msge="Invalid password"
            return render(request,"register.html",{"b":msge})
        else:
            
            request.session["det"]=[username,firstname,lastname,gmail,password,repassword]
            send_mail("otp validation","Your otp is 56789",settings.EMAIL_HOST_USER,[gmail,])
            return render(request,"indexx.html")
            
            user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=gmail,password=password)
            user.save();

        return redirect("/")

    else:
        return render(request,"register.html")  


def login(request):
    if request.method=="POST":
        user=request.POST["uname"]
        password=request.POST["pname"]
        check=auth.authenticate(username=user,password=password)
        if check is not None:
            auth.login(request,check)
            response= redirect("/")
            response.set_cookie("pas",password)
            return response
        else:
            msge="Invalid password or username"
            return render(request,"login.html",{"msg":msge})
    else:
        return render(request,"login.html")  


def logout(request):
    auth.logout(request)
    response= redirect("/")
    response.delete_cookie("pas")
    response.delete_cookie("price")
    return response
def detail(request):
    return render(request,"detail.html")




def otp(request):
    if request.method=="POST":
        n1=request.POST["n1"]
        n2=request.POST["n2"]
        n3=request.POST["n3"]
        n4=request.POST["n4"]
        n5=request.POST["n5"]
        otp=n1+n2+n3+n4+n5
        if otp=="56789":
            li=request.session["det"]
            user=User.objects.create_user(username=li[0],first_name=li[1],last_name=li[2],email=li[3],password=li[4])
            user.save();
            return redirect("/")
        else: 
            a="Enter otp again"   
            return render(request,"indexx.html",{"c":a})
    else:    
        return render(request,"indexx.html")


