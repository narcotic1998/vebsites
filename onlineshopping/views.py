from django.shortcuts import render

def online_shopping(request):
    context = {
        "title":"Online Shopping",
    }
    return render(request,"onlineshopping/onlineshopping.html",context)
def electronics(request):
    context = {
        "title":"Electronics"
    }
    return render(request,"onlineshopping/electronics.html",context)

def fashion(request):
    context = {
        "title":"Fashion"
    }
    return render(request,"onlineshopping/fashion.html",context)
