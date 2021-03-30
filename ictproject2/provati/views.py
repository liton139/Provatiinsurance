from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from provati.EmailBackEnd import EmailBackEnd


def homepage(request):
    return render(request,"picladmin/home_content.html")

def showDemo(request):
    return render(request,"show.html")


def showlogin(request):
    return render(request,"login.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h1>METHOD NOT Allowed</h1>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            return HttpResponseRedirect("/admin_home")
        else:
            messages.error(request,"InValid Login details")
            return HttpResponseRedirect("/")

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("user :" +request.user.email + "user type : " +request.user.user_type)
    else:
        return HttpResponse("please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")