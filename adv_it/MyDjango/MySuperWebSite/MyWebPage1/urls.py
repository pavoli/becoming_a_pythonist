# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
