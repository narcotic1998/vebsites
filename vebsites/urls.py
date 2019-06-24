from django.conf.urls import url , include
from . import views

urlpatterns = [
    url(r'^$', views.vebsites, name="vebsites"),
    url(r'online-shopping/', include('onlineshopping.urls',namespace="onlineshopping")),
    url(r'entertainment/', include('entertainment.urls',namespace="entertainment")),
    url(r'sports/', include('sports.urls',namespace="sports")),
    url(r'booking/', include('booking.urls',namespace="booking")),
    url(r'education/', include('education.urls',namespace="education")),
]
