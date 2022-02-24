from django.shortcuts import render
from enroll.models import Student

# Create your views here.

def studentinfo(request):
    stud= Student.objects.all()  #QuerySet
    print('My output',stud)
    return render(request,'enroll/studetails.html',{'stu':stud}) #transferring stud to template file
    

