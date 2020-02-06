from django.contrib import admin
from django.urls import include, path
from . import views


app_name = 'billboards'

urlpatterns = [
    #path('', views.billboards, name="list"),
    path('', views.listtest, name="listtest"),
]
