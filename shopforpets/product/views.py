
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
    return render(request,"detail.html",{"pro":data,"total":total})
def cmt(request):
    comments=request.POST["comment"]
    name=request.POST["user"]
    id=request.POST["id"]
    mt=comment.objects.create(cmt=comments,name=name,pro_id=id)
    mt.save();



    return redirect("/product/?id="+id)