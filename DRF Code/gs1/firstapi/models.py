from django.db import models

# Create your models here.

class Student(models.Model):
    name= models.CharField(("name"), max_length=50) 
    roll = models.IntegerField(("roll"))
    city = models.CharField(("city"), max_length=100)
    
    # email = models.CharField(max_length=20) optional will make field default
    
