from django.shortcuts import render
from django.http import HttpResponse
#from .models import Billboard, Account
from . import forms

def login(request):
    return render(request, 'Registration/login.html')

def accounts(request):
    return render(request, 'accounts/accounts.html')

def billboard_list(request):
    #billboards = Billboard.objects.all().order_by('rating')
    #return render(request, 'accounts/billboard_list.html', {'billboards': billboards})
    return True
def registration(request):
    return render(request, 'Registration/registration.html' )

def test(response):
    #form = forms()
    #return render(response, 'accounts/test.html', {'form': form})
    return True
#the billboard detail function below is messed up
def billboard_detail(request, name):
    #billboard = Billboard.objects.get(name=name)
    #return render(request,'accounts/billboard_detail.html', {'billboard': billboard})
    return True
# Create your views here.
