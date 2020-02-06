from django.shortcuts import render
from .models import Billboard
from .models import rent
from .forms import rentRequestForm
def billboards(request):
    billboards = Billboard.objects.all().order_by('rating')
    return render(request, 'billboards/billboard_list.html',{'billboards':billboards})
def BillboardList(request):
    billboards = Billboard.objects.all().order_by('rating')
    return render(request, 'billboards/billboard_list.html',{'billboards':billboards})
def addBillboard(request):
    return True
def detail(request, Billboard_id):
    singleBillboard=Billboard.objects.get(id=Billboard_id) 
    return render(request,'billboards/billboardDetail.html',{'singleBillboard':singleBillboard} )
    
def sendRentRequest(request):
    if request.method=="POST":
        form = rentRequestForm(request.POST)
        if form.is_valid():
            startDate = form.cleaned_data["startDate"]
            endDate = form.cleaned_data["endDate"]
            advertisementType = form.cleaned_data["advertisementType"]
            billboard = form.cleaned_data["billboard"]
            newBillboard = rent(startDate=startDate,endDate=endDate, advertisementType=advertisementType,billboard=billboard)
            newBillboard.save()
    else:
        form = rentRequestForm()
    return render(request, "billboards/rentRequestForm.html", {'form':form})   
# Create your views here.
