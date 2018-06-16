#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: 韩朝彪
# @Date  : 2018/6/15
# @Desc  :
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.index),
    url(r"^pay/$", views.pay),
    url(r"^check_pay/$", views.check_pay),
]