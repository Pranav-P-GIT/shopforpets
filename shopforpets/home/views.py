from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import PetProduct



# Create your views here.
def index(request):
    data=PetProduct.objects.all

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
        elif echeck:
            msge="email is already taken"
            return render(request,"register.html",{"b":msge}) 
        elif password=="" or password!=repassword:
            msge="Invalid password"
            return render(request,"register.html",{"b":msge})
        else:
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
            return redirect("/")
        else:
            msge="Invalid password or username"
            return render(request,"login.html",{"msg":msge})
    else:
        return render(request,"login.html")  


def logout(request):
    auth.logout(request)
    return redirect ("/")
def detail(request):
    return render(request,"detail.html")


