# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def sports(request):
    context = {
        "title":"Sports",
    }
    return render(request,"sports/sports.html",context)
