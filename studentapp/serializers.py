from .models import Student
from rest_framework.serializers import ModelSerializer
from django.db.models import fields

class StudentSerializer(ModelSerializer):
    
    class Meta:
        model = Student
        fields = ('name', 'id','age', 'email', 'mobile_no')
        
        