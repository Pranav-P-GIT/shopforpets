
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User


def detail(request):
    return render(request,"detail.html")