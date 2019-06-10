# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def online_shopping(request):
    context = {
        "title":"Online Shopping",
    }
    return render(request,"onlineshopping/onlineshopping.html",context)
