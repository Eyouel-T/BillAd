from django.contrib import admin
from django.urls import include, path
from . import views


app_name = 'billboards'

urlpatterns = [
    ('', views.billboards, name="list"),
]
#this is a git test