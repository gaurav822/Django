from django.db import models

# Create your models here.

class Person(models.Model):
    pid=models.IntegerField()
    pname=models.CharField(max_length=20)
    pemail=models.CharField(max_length=30)
    ppass=models.CharField(max_length=20)
