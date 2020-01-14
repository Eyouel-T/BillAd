from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.EmailField(default='noemail@empty.com')
    password = models.CharField(max_length=100)

