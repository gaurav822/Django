from django.db import models

# Create your models here.

class Student(models.Model):
    stuid=models.IntegerField()
    stuname=models.CharField(max_length=20)
    stuemail=models.CharField(max_length=30)
    stupass=models.CharField(max_length=20)

    def __str__(self):
        return self.stuname

        #return str(self.stuid)

