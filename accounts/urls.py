from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.accounts),
    path('billboards/', views.billboard_list),
    path('list/',views.billboard_list),


]