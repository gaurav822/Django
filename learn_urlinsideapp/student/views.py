from django.shortcuts import render
from django.http import HttpResponse

def study(request):
    return HttpResponse('Studying..')

def play_basketball(request):
    return HttpResponse('Play basketball')
