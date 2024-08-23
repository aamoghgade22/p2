from rest_framework import serializers
from .models import Student, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status']
        read_only_fields = ['user']  


# FOR GENERIC VIEWSET

class StudentSerializer(serializers.ModelSerializer):
    branch = serializers.CharField(source='division.branch', read_only=True)
    class Meta:
        model=Student
        fields="__all__"