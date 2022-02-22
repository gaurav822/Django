import io
from api.models import Product,Users
from api.serializers import ProductSerializer,UserSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def user_detail(request,pk):
    user = Users.objects.get(id=pk)
    serializer = UserSerializer(user)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

def user_list(request):
    user = Users.objects.all()
    serializer = UserSerializer(user,many=True)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

def product_detail(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')


def product_list(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product,many=True)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

@csrf_exempt
def user_create(request):
    if(request.method=='POST'):
        json_data = request.body
        stream= io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        serialzier= UserSerializer(data=pythondata)
        if serialzier.is_valid():
            serialzier.save()
            res = {'msg' : 'User created'}  
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serialzier.errors)
        return HttpResponse(json_data,content_type='application/json')
            
 


