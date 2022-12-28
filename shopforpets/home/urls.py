from django.urls import path
from.import views
from.import feed
urlpatterns = [
    path("",views.index,name="homepage"),
    path("test",views.test),
    path("login/",views.login,name="loginpage"),
    path("register/",views.register,name="registerpage"),
    path("Logout/",views.logout,name="logoutpage"),
    path("feed/",feed.LatestNews(),name="feedpage"),
    path("otp/",views.otp,name="OTPpage"),
    
    ]