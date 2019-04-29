from django.shortcuts import render

# Create your views here.
from school.models import School
from school.serializers import SchoolSerializer

from rest_framework import viewsets


# Create your views here.
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer