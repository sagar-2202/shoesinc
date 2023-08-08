from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from home.models import personinfo, signInfo
# Create your views here.

def index(request):
    return render(request,'index.html')

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        #check credentials
        if user is not None:
            login(request, user)
            return redirect("/personal")
        else:
            return render(request,'login.html')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return render(request,'index.html')

def contactinfo(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        inf=personinfo(name=name,email=email,phone=phone,desc=desc)
        inf.save()
    return render(request,'contact.html')

def personalinfo(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request,'personal.html')

def signupUser(request):
    if request.method=="POST":
        username_signup=request.POST.get('username_signup')
        email_signup=request.POST.get('email_signup')
        password_signup=request.POST.get('password_signup')
        user_signup=User.objects.create_user(username=username_signup,email=email_signup,password=password_signup)
        user_signup.save()
        return render(request,'signup.html')
    return render(request,'signup.html')