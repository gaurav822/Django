from importlib.metadata import requires
from rest_framework import serializers

from api.models import Student

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    roll=serializers.IntegerField()
    address=serializers.CharField(max_length=100)

    def create(self,validate_data):
        return Student.objects.create(**validate_data)
        

