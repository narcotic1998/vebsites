# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def education(request):
    context = {
        "title":"Education"
    }
    return render(request,"education/education.html",context)
