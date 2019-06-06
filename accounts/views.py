from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.views import LoginView
from accounts.forms import EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as django_logout

def login_user(request):
    username = password = ''
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user:
            login(request,user)
            return redirect("/accounts/profile")
        else:
            messages.info(request,"Incorrect Username or Password")
            return redirect("/accounts/login")
    else:
        context={"login":"active","title":"Login"}
        return render(request,"accounts/login.html",context)

def register(request):
    if request.method=="POST":
        uservalue = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email= request.POST['email']
        passwordvalue1 = request.POST['password1']
        passwordvalue2 = request.POST['password2']
        if passwordvalue1 == passwordvalue2:
            if len(passwordvalue1) < 8:
                messages.info(request,"Passwords should have atleast 8 Characters")
                context= {
                'title':"Register",
                "register":"active",
                "username":uservalue,
                "first_name":firstname,
                "last_name":lastname,
                "email":email,
                }
                return render(request, 'accounts/register.html', context)
            else:
                try:
                    user= User.objects.get(username=uservalue)
                    messages.info(request,"The username you entered has already been taken. Please try another username")
                    context= {
                    'title':"Register",
                    "register":"active",
                    "first_name":firstname,
                    "last_name":lastname,
                    "email":email,
                    }
                    return render(request, 'accounts/register.html', context)
                except User.DoesNotExist:
                    try:
                        user = User.objects.get(email=email)
                        messages.info(request,"Email already exists, please Login")
                        return redirect("/accounts/login")
                    except User.DoesNotExist:
                        user= User.objects.create_user(uservalue, password= passwordvalue1, email=email,first_name=firstname,last_name=lastname)
                        user.save()
                        messages.info(request,"Successfully Registered")
                        return redirect("/accounts/login")
        else:
            messages.info(request,"Passwords do not match")
            context= {
            'title':"Register",
            "register":"active",
            "username":uservalue,
            "first_name":firstname,
            "last_name":lastname,
            "email":email,
            }
            return render(request, 'accounts/register.html', context)

    else:
        context = {"register":"active","title":"Register"}
        return render(request,"accounts/register.html",context)


def profile(request):
    user = request.user
    if user.is_authenticated:
        context = {"title":"Profile","user":request.user,"dashboard":"active"}
        return render(request,"accounts/profile.html",context)
    else:
        messages.info(request,"You are not logged in ")
        return redirect("/accounts/login")

def info(request):
    user = request.user
    if user.is_authenticated:
        context = {"info":"active","title":"My Account"}
        return render(request,"accounts/info.html",context)
    else:
        messages.info(request,"You are not logged in ")
        return redirect("/accounts/login")

def edit_profile(request):
    user = request.user
    if user.is_authenticated:
        if request.method=="POST":
            form = EditProfileForm(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                messages.info(request,"Profile Updated")
                return redirect("/accounts/profile/info")
        else:
            form = EditProfileForm(instance=request.user)
            context = {"title":"Edit Profile","info":"active","form":form}
            return render(request,"accounts/edit_profile.html",context)
    else:
        messages.info(request,"You are not logged in ")
        return redirect("/accounts/login")

def change_password(request):
    user = request.user
    if user.is_authenticated:
        if request.method=="POST":
            form = PasswordChangeForm(data=request.POST,user=request.user)
            if form.is_valid():
                form.save()
                messages.info(request,"Password Changed Successfully, Please Login again!!")
                return redirect("/accounts/login")
        else:
            form = PasswordChangeForm(user=request.user)
            context = {"title":"Change Password","info":"active","form":form}
            return render(request,"accounts/change_password.html",context)
    else:
        messages.info(request,"You are not logged in ")
        return redirect("/accounts/login")

def logout(request):
    django_logout(request)
    messages.info(request,"Logged out Successfully")
    return redirect("/accounts/login")
