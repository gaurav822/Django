from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name= serializers.CharField( max_length=50) 
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)


# class StudentForm(forms.Form):
#     name= forms.CharField(("name"), max_length=50) 
#     roll = forms.IntegerField(("roll"))
#     city = forms.CharField(("city"), max_length=100)

