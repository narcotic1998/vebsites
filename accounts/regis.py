def register(request):
    if request.method=="POST":
        firstname= form.cleaned_data.get("first_name")
        lastname= form.cleaned_data.get("last_name")
        emailvalue= form.cleaned_data.get("email")
        uservalue= form.cleaned_data.get("username")
        passwordvalue1= form.cleaned_data.get("password1")
        passwordvalue2= form.cleaned_data.get("password2")
        if passwordvalue1 == passwordvalue2:
            try:
                user= User.objects.get(username=uservalue)
                context= {'error':'The username you entered has already been taken. Please try another username.',
                'title':"title",
                "register":"active",
                'first_name':firstname,
                }
                return render(request, 'accounts/register.html', context)
            except User.DoesNotExist:
                user= User.objects.create_user(uservalue, password= passwordvalue1, email=emailvalue)
                user.save()
                messages.info(request,"Successfully Registered")
                return redirect("/accounts/login")

    else:
        context = {"register":"active","title":"Register"}
        return render(request,"accounts/register.html",context)
