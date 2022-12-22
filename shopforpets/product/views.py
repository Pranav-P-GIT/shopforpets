
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.db import models
from home.models import PetProduct
from .models import comment


def detail(request):
    id=request.GET["id"]
    data=PetProduct.objects.get(id=id)
    
    total=int(data.price)-(int(data.price)*int(data.discount)/100)
    if "his" in request.session:
        if id in request.session["his"]:
            request.session["his"].remove(id)    
            request.session["his"].insert(0,id)  
        else:
            request.session["his"].insert(0,id)
        if len(request.session["his"])>4:
                request.session["his"].pop()
        print(request.session["his"])
        recent=PetProduct.objects.filter(id__in=request.session["his"])
        print(recent)
        request.session.modified=True
        return render(request,"detail.html",{"pro":data,"total":total,"recent":recent})
                

        
    else:
        print("hello")
        request.session["his"]=[id]
        print(request.session["his"])
        return render(request,"detail.html",{"pro":data,"total":total})
        
  
    





def cmt(request):
    comments=request.POST["comment"]
    name=request.POST["user"]
    id=request.POST["id"]
    mt=comment.objects.create(cmt=comments,name=name,pro_id=id)
    mt.save();



    return redirect("/product/?id="+id)