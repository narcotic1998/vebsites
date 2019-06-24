from django.conf.urls import url , include
from . import views

urlpatterns = [
    url(r'online-shopping/$', include('onlineshopping.urls',namespace="onlineshopping")),
    url(r'entertainment/$', include('entertainment.urls',namespace="entertainment")),
]
