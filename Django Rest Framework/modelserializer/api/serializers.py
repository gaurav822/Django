from rest_framework import serializers
from .models import Student


#Validators
def start_with_r(value):
    if(value[0].lower()!='r'):
        raise serializers.ValidationError('Name should start with R')

class StudentSerializer(serializers.ModelSerializer):
    # name=serializers.CharField(read_only=True) #it means name cannot be updated or created
    name=serializers.CharField(validators=[start_with_r])
    class Meta:
        model=Student
        fields=['id','name','roll','city']

        #to make multiple read-only true
        # read_only_fields=['name','roll']

        #another way to make readonly
        # extra_kwargs={'name':{'ready_only':True}}

    #Field Level Validation

    def validate_roll(self,value):
        if(value >= 200):
            raise serializers.ValidationError('Seat Full')
        return value
    
    #Object Level Validation    

    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower()=='veeru' and ct.lower()!='kathmandu':
            raise serializers.ValidationError('City must be Kathmandu')
        return data
        
        

    
    
