from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import Billboard, Account
from . import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from billboards.forms import addBillboardForm
from billboards.models import Billboard
from .forms import registerUserForm
from accounts.forms import signin
from billboards.models import rent
from .models import Account
#completely confusing code below
"""def addBillboard(request):
    if request.method=="POST":
        Billboard = Billboard(request.POST)
        if Billboard.is_valid():
            Billboard.save()
    else:
        AddBillboard = Billboard()
    return render(request,{'AddBillboard':addBillboard})"""
#completely confusing code above
#just ignore it for now
def owner(request):
    rents= rent.objects.all()  
    return render(request,"accounts/owner.html",{'rents':rents})
def add(request):
    if request.method == 'POST':
        form = addBillboardForm(request.POST)
        if form.is_valid():
            photo = form.cleaned_data["photo"]
            name= form.cleaned_data["name"]
            location = form.cleaned_data["location"]
            owner = form.cleaned_data["owner"]
            price = form.cleaned_data["price"]
            rating = form.cleaned_data["rating"]
            length = form.cleaned_data["length"]
            width = form.cleaned_data["width"]
            rent = form.cleaned_data["rent"]
            newBillboard = Billboard(primary_photo=photo,name=name, location=location,owner=owner,price=price,rating=rating,length=length,width=width,rent=rent)
            newBillboard.save()
    else:
        form = addBillboardForm()
    return render(request, "accounts/addBillboard.html", {'form':form})

def registrationtest(request):
    if request.method == 'POST':
        form = registerUserForm(request.POST)
        if form.is_valid():
            #profile_picture = form.cleaned_data["profile_picture"]
            name= form.cleaned_data["name"]
            phone_number = form.cleaned_data["phone_number"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            newUser = Account(name=name, phone_number=phone_number,email=email,password=password)
            newUser.save()
    else:
        form = registerUserForm()
    return render(request, "accounts/registrationtest.html", {'form':form})
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
def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in,
            user = form.get_user()
            login(request, user)
            return redirect('billboards:BillboardList')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/signin.html',{'form':form})

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
