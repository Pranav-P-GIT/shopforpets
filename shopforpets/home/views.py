from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request,"index.html")
def test(request):

    val="php"
    return render(request,"test.html",{"a":val,"b":"object oriented"})
def register(request):
    return render(request,"register.html")  
def login(request):
    return render(request,"login.html")  
def snd(request):
    user=request.GET["uname"]
    password=request.GET["pname"]
    check=auth.authenticate(username=user,password=password)
    if check is not None:
        auth.login(request,check)
    else:
        msge="Invalid password or username"
        return render(request,"test.html",{"a":msge})
    return redirect("/")
         
def send(request):
    username=request.GET["uname"]
    firstname=request.GET["fname"]
    lastname=request.GET["lname"]
    gmail=request.GET["mail"]
    password=request.GET["password"]
    repassword=request.GET["ppassword"]
    ucheck=User.objects.filter(username=firstname)
    echeck=User.objects.filter(email=gmail)
    if ucheck:
        msg="username is already taken"
        return render(request,"test2.html",{"a":msg})
    elif echeck:
        msge="email is already taken"
        return render(request,"test2.html",{"b":msge}) 
    elif password=="" or password!=repassword:
         msge="Invalid password"
         return render(request,"test2.html",{"b":msge})
    else:
        user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=gmail,password=password)
        user.save();

        return redirect("/")


    
