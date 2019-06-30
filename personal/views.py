from django.shortcuts import render

def index(request):
    context = {"home":"active","title":"Home"}
    return render(request, 'personal/home.html',context)
def contact(request):
    context = {"contact":"active","title":"Contact"}
    user = request.user
    if user.is_authenticated:
        return render(request, 'personal/contact1.html',context)
    else:
        return render(request,'personal/contact.html',context)
