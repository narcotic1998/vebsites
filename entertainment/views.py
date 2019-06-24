# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def entertainment(request):
    context = { "title" : "Entertainment" }
    return render(request,"entertainment/entertainment.html",context)
