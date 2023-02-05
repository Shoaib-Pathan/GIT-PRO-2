from django.shortcuts import render
from rest_framework import viewsets
from .serialiers import StudentSerializer
from .models import Student


# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()