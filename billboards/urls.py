from django.contrib import admin
from django.urls import include, path
from . import views


app_name = 'billboards'

urlpatterns = [
    #path('', views.billboards, name="list"),
    path('', views.BillboardList, name="BillboardList"),
    path('rent/', views.sendRentRequest, name="rentRequestForm"),
    path('detail/', views.detail, name="detail"),
]
