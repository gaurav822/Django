from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password= models.CharField(max_length=20)
    address= models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price=models.IntegerField()
    category=models.CharField(max_length=50)


