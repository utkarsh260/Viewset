from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework import status

# Create a viewset

class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    
    def list(self, request):
        serializer = StudentSerializer(self.queryset, many = True)
        return Response(serializer.data)
    
    
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_201_CREATED)
        
    
    def retrieve(self, request, pk=None):
        user= get_object_or_404(self.queryset, pk=pk)
        serializer = StudentSerializer(user)
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        student = get_object_or_404(Student.objects.all(), pk=pk)
        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        student = get_object_or_404(Student.objects.all(), pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        

