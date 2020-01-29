from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import Billboard, Account
from . import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in,
            login(request,user)
            # ie.redirect the user to another page
    else:
        form = UserCreationForm()
    return render(request, 'accounts/registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in,
            user =form.get_user()
            login(request, user)
            return redirect('billboards:list')
    else:
        form =AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})


def accounts(request):
    return render(request, 'accounts/accounts.html')


def billboard_list(request):
    return redirect('billboards:list')
    # billboards = Billboard.objects.all().order_by('rating')
    # return render(request, 'accounts/billboard_list.html', {'billboards': billboards})
    return True


def test(response):
    # form = forms()
    # return render(response, 'accounts/test.html', {'form': form})
    return True
    # the billboard detail function below is messed up


def billboard_detail(request, name):
    # billboard = Billboard.objects.get(name=name)
    # return render(request,'accounts/billboard_detail.html', {'billboard': billboard})
    return True
# Create your views here.
