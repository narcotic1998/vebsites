# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def vebsites(request):
    context = {
        "title":"Vebsites"
    }
    return render(request,"vebsites/vebsites.html",context)
