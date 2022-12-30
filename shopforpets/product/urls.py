from django.urls import path
from .import views

urlpatterns = [    
    path("",views.detail2,name="detailpage"),
    path("cmt/",views.cmt,name="commentpage"),
    path("email/",views.test,name="emailpage"),
    path("search/",views.search,name="searchpage"),
    path("auto/",views.autosearch,name="autopage"),

]
