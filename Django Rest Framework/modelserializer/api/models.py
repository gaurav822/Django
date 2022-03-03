from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=40)
    number=models.IntegerField(max_length=10)
    address=models.CharField(max_length=100)

class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    city=models.CharField(max_length=100)