from django.db import models

class Billboard(models.Model):
    primary_photo= models.ImageField(default='default.png', blank=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    #id = models.IntegerField()
    owner = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    rating = models.IntegerField(default=0)
    length = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    rent = models.CharField(default="none",max_length=100)
# Create your models here.
class rent(models.Model):
    startDate = models.DateField()
    endDate = models.DateField()
    advertisementType = models.CharField( max_length=200) 
    billboard = models.CharField(max_length=200)