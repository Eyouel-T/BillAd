from django import forms

class addBillboardForm(forms.Form):
    photo = forms.ImageField()
    name = forms.CharField(label="Name", max_length=200)
    location = forms.CharField(label="loaction", max_length=200)
    owner = forms.CharField(label="owner", max_length=200)
    price = forms.IntegerField()
    rating = forms.IntegerField()
    length = forms.IntegerField()
    width = forms.IntegerField()
    rent = forms.CharField(label="rent",max_length=100)
class rentRequestForm(forms.Form):
    startDate = forms.DateField()
    endDate = forms.DateField()
    advertisementType = forms.CharField(label="Advertisement", max_length=200) 
    billboard = forms.CharField(label="billboard", max_length=200)