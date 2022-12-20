from django.urls import path
from .import views

urlpatterns = [    
    path("",views.detail,name="detailpage"),
    path("cmt/",views.cmt,name="commentpage")

]
