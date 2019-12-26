from django.shortcuts import render
from django.http import HttpResponse
from .models import Billboard

def accounts(request):
    return render(request,'Registration/login.html')

def billboard_list(request):
    billboards = Billboard.objects.all().order_by('rating')
    return render(request, 'accounts/billboard_list.html', {'billboards': billboards})



# Create your views here.
