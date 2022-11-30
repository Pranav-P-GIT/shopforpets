from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
def test(request):

    val="php"
    return render(request,"test.html",{"a":val,"b":"object oriented"})    
