from django.http import HttpResponse
from django.shortcuts import render, redirect


def homepage(request):
    #return HttpResponse(' konjiye homepage')
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return redirect('accounts:login')

def BillboardList(request):
    return redirect('billboards:BillboardList')
def home(request):
    return redirect('homepage.html')


