from django import forms

"""
class RegisterAnAccount(forms.Form):
    #profilePicture = forms.ImageField(label="Image")
    name = forms.CharField(max_length=100,label="Name")
    phoneNumber = forms.CharField(max_length=15, label="Phone Number")
    email = forms.EmailField(label="Email")
    password = forms.CharField(max_length=100, label="Password")
"""
class signin(forms.Form):
    name=forms.CharField(max_length=100,label="Userame")
    password = forms.CharField(max_length=100, label="Password")
class registerUserForm(forms.Form):
    #profile_picture = forms.ImageField()
    name =  forms.CharField(max_length=100)
    phone_number =  forms.IntegerField()
    email =  forms.EmailField()
    password =  forms.CharField(max_length=100)