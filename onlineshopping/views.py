from django.shortcuts import render

def online_shopping(request):
    context = {
        "title":"Online Shopping",
    }
    return render(request,"onlineshopping/onlineshopping.html",context)
