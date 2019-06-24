from __future__ import unicode_literals

from django.shortcuts import render

def booking(request):
    context = {
        "title":"Booking"
    }
    return render(request,"booking/booking.html",context)
