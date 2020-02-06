from django.db import models

class Account(models.Model):
    #profile_picture = models.ImageField(default='default.png', blank=True)
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.EmailField(default='noemail@empty.com')
    password = models.CharField(max_length=100)

class Advertiser(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.EmailField(default='noemail@empty.com')
    password = models.CharField(max_length=100)
    rented_billboards= models.CharField(max_length=100)
    rating = models.IntegerField()

class Owner(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.EmailField(default='noemail@empty.com')
    password = models.CharField(max_length=100)
    rating = models.IntegerField()
    preferred_content=models.CharField(max_length=100)
class Adminstrator(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.EmailField(default='noemail@empty.com')
    password = models.CharField(max_length=100)
    Adminstrator_id = models.IntegerField()