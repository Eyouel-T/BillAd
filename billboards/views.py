from django.shortcuts import render
from .models import Billboard

def billboards(request):
    billboards = Billboard.objects.all().order_by('rating')
    return render(request, 'billboards/billboard_list.html',{'billboards':billboards})
def listtest(request):
    billboards = Billboard.objects.all().order_by('rating')
    return render(request, 'billboards/listtest.html',{'billboards':billboards})
# Create your views here.
