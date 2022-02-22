from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=50)
    password= serializers.CharField(max_length=20)
    address= serializers.CharField(max_length=100)

    def create(self,validate_data):
        return Users.objects.create(**validate_data)

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    price=serializers.IntegerField()
    category=serializers.CharField(max_length=50)