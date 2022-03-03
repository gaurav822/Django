from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# @api_view()   #By default GET is provided
# def hello_world(request):
#     return Response({'msg':'Hello World'})

#we can mention explicitly    
# @api_view(['GET'])  
# def hello_world(request):
#     return Response({'msg':'Hello World'})


# @api_view(['POST'])
# def hello_world(request):
#     if request.method=='POST':
#         print(request.data)
#         return Response({'msg':'This is Post Request'})

@api_view(['GET','POST'])
def hello_world(request):
    if request.method=='GET':
        return Response({'msg':'This is Get Request'})
    if request.method=='POST': 
        print(request.data)
        return Response({'msg':'This is Post Request','data':request.data})
    

