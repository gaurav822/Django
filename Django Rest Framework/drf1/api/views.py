
import imp
from django.shortcuts import render
from api.models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt

# Model Object - Single Student Data

def student_detail(request,pk):
    stu= Student.objects.get(id=pk)
    serializer= StudentSerializer(stu)
    # print(serializer.data)
    json_data=JSONRenderer().render(serializer.data)
    # print(json_data)
    return HttpResponse(json_data,content_type='application/json')

    #return JsonResponse(serializer.data) add ,safe=False if it is not returning single model or it is non-dict object



# Query Set - All Student Data

def student_all(request):
    stu= Student.objects.all()
    serializer= StudentSerializer(stu,many=True)
    return JsonResponse(serializer.data,safe=False)


@csrf_exempt
def student_create(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        serializer= StudentSerializer(data=pythondata)
        if(serializer.is_valid()):
            serializer.save() 
            res={'msg':'Data created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
        return JsonResponse(serializer.errors)


         

