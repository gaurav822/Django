from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('Home Page')

def learn_django(request):  #we can write req as well
    return HttpResponse('<h1>Hello world</h1>') # we can write html as well instead of plain text

def learn_python(request):
    a='<h1>Hello Learn Python</h1>'
    return HttpResponse(a)

def learn_math(request):
    a=10+10
    return HttpResponse(a)

def learn_format(request):
    a='Gaurav Dahal'
    return HttpResponse(f'Hello how are you Mr. {a}')
