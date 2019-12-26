from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    #return HttpResponse(' konjiye homepage')
    return render(request, 'homepage.html')

def about(request):
    return HttpResponse('about')

def loginsub(request):
    return render(request, 'loginsub.html')

def list(request):
    return render(request, 'list.html')



