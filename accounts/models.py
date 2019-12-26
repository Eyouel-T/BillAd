from django.db import models


class Account(models.Model):
    profilePicture = models.ImageField()
    name = models.TextField(max_length=100)
    email = models.EmailField(default="email@mail.com")
# Create your models here.

    def __str__(self):
        return self.name


class Billboard(models.Model):
    #photo1 = models.ImageField()
    #photo2 = models.ImageField()
    #photo3 = models.ImageField()
    #photo4 = models.ImageField()
    #price = models.IntegerField()
    name = models.TextField(max_length=30)
    location = models.TextField(max_length=20)
    Owner = models.TextField
    price = models.IntegerField(default=0)
    rating = models.IntegerField()
    rentStartDate = models.DateField(auto_now=False, auto_now_add=False)
    rentEndDate = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
