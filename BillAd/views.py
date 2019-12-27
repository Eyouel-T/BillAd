from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    #return HttpResponse(' konjiye homepage')
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')
"""
this bottom function is just used for  testing 
"""
def loginsub(request):
    return render(request, 'loginsub.html')

def list(request):
    return render(request, 'list.html')



