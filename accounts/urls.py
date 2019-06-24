from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)

urlpatterns = [
    url(r'^login/$',views.login_user,name='login'),
    url(r'^register/$',views.register,name='register'),
    url(r'^profile/info$',views.info,name="info"),
    url(r'^profile/edit$',views.edit_profile,name="edit_profile"),
    url(r'^logout/$',views.logout,name="logout"),
    url(r'^password/$',views.change_password,name="change_password"),
    url(
    r'^forgot_password/$',
    password_reset,
    {"template_name":"accounts/forgot_password.html"},name='reset-password'
    ),
    url(
    r'^password_reset/done/$',
    password_reset_done,
    {"template_name":"accounts/password_reset_done.html"},
    name='password_reset_done'
    ),
    url(
    r'^password_reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,23})/$',
    password_reset_confirm,
    {"template_name":"accounts/password_reset_confirm.html"},
    name='password_reset_confirm'
    ),
    url(
    r'^password_reset/complete/$',
    password_reset_complete,
    {"template_name":"accounts/password_reset_complete.html"},
    name='password_reset_complete'),
    ]
