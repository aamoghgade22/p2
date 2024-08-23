from rest_framework import serializers
from .models import Student, Task,Book

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status']
        read_only_fields = ['user']  

# FOR generics
class StudentSerializer(serializers.ModelSerializer):
    branch = serializers.CharField(source='division.branch', read_only=True)
    class Meta:
        model=Student
        fields="__all__"

# For GenericViewSet
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
