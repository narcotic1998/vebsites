from django.conf.urls import url , include
from . import views

urlpatterns = [
    url(r'^$', views.online_shopping,name="home"),
    url(r'electronics/$',views.electronics,name="electronics"),
    url(r'fashion/$',views.fashion,name="fashion"),
]
