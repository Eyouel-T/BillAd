from django.contrib import admin
from django.urls import include, path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('', views.accounts),
    path('billboards/', views.billboard_list),
    path('registration/', views.registration, name="registration"),
    path('login/', views.login),
    path('detail/', views.billboard_detail),

]

