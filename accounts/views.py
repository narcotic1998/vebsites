from django.shortcuts import render, redirect
from accounts.forms import EditProfileForm,ProfileForm,RegistrationForm,ChangePasswordForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as django_logout
from django.urls import reverse
from django import forms

def login_user(request):
    username = password = ''
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user:
            login(request,user)
            return redirect(reverse("vebsites"))
        else:
            context = {"username":username,"title":"Login","login":"active"}
            messages.info(request,"Incorrect Username or Password")
            return render(request,"accounts/login.html",context)
    else:
        context={"login":"active","title":"Login"}
        return render(request,"accounts/login.html",context)

def register(request):
    if request.method=="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"Successfully Registered")
            return redirect(reverse('login'))
    else:
        form= RegistrationForm()

    context = {"title":"Register","register":"active","form":form}
    return render(request,"accounts/register.html",context)

def info(request):
    context = {"info":"active","title":"My Account"}
    return render(request,"accounts/info.html",context)

def edit_profile(request):
    if request.method=="POST":
        form = EditProfileForm(request.POST,instance=request.user)
        form1 = ProfileForm(request.POST,instance=request.user.profile)
        if form.is_valid():
            form.save()
            if form1.is_valid():
                form1.save()
                messages.info(request,"Profile Updated")
                return redirect(reverse("info"))
    else:
        form = EditProfileForm(instance=request.user)
        form1= ProfileForm(instance=request.user.profile)
    context = {"title":"Edit Profile","info":"active","form":form,"form1":form1}
    return render(request,"accounts/edit_profile.html",context)

def change_password(request):
    if request.method=="POST":
        form = ChangePasswordForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            django_logout(request)
            messages.info(request,"Password Changed Successfully, Please Login again!!")
            return redirect(reverse('login'))

    else:
        form = ChangePasswordForm(user=request.user)

    context = {"title":"Change Password","info":"active","form":form}
    return render(request,"accounts/change_password.html",context)

def logout(request):
    django_logout(request)
    messages.info(request,"Logged out Successfully")
    return redirect(reverse("login"))
