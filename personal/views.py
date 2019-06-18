from django.shortcuts import render

def index(request):
    context = {"home":"active","title":"Home"}
    return render(request, 'personal/home.html',context)
def contact(request):
    context = {"contact":"active","title":"Contact"}
    return render(request, 'personal/contact.html',context)
