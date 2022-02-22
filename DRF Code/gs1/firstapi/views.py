from django.shortcuts import render
from firstapi.models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer 
from django.http import HttpResponse, JsonResponse

#Model Object - Single Student data

def student_detail(request,pk):
    stu=Student.objects.get(id=pk)  # model object which is complex data type  
    # print(stu) 
    serializer= StudentSerializer(stu)  # converting to python object
    # print(serializer)
    # print(serializer.data)
    json_data= JSONRenderer().render(serializer.data)  #converting to json data
    # print(json_data)
    return HttpResponse(json_data,content_type='application/json') #sending json to client

    # return JsonResponse(serializer.data) shortcut by default safe= True

#Query Set - All Student Data

def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')
    # return JsonResponse(serializer.data,safe=False)
    # safe is false since it is not dict type which is returning List

