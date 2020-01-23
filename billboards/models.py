from django.db import models

class Billboard(models.Model):
    primary_photo= models.ImageField(default='default.png', blank=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    #id = models.IntegerField()
    owner = models.CharField(max_length=100)
    price = models.IntegerField()
    rating = models.IntegerField()
    length = models.IntegerField()
    width = models.IntegerField()
    rent = models.CharField(max_length=100)
# Create your models here.
