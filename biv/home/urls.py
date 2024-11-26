# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url
from views import Login, Register

urlpatterns = patterns(
    '',
     url(r'^login$',Login.as_view(), name='login'),
     url(r'^register',Register.as_view(), name='register'),
)
