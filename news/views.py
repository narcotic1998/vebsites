# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def news(request):
    context = {
        "title":"News"
    }
    return render(request,"news/news.html",context)
