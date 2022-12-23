from django.urls import path
from .import views

urlpatterns = [    
    path("",views.detail2,name="detailpage"),
    path("cmt/",views.cmt,name="commentpage")

]
