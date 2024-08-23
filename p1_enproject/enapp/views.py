from urllib import response
from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, Student, Task
from .serializers import BookSerializer, StudentSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.response import Response

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username # customize token
        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class =MyTokenObtainPairSerializer


##  MODEL VIEWSET - Only 3 lines

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    #overriding some methods
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Task.objects.filter(user=user)
        else:
            return Task.objects.none() 
       
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

@login_required
def index(request):
    user = request.user
    tasks = Task.objects.filter(user=user)
    return render(request, 'home.html', {'tasks': tasks})

##  GENERICS in viewset

# FOR GET , CREATE
class StudentGeneric (generics.ListAPIView,generics.CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
# FOR UPDATE AND DELETE
class StudentGeneric1 (generics.UpdateAPIView,generics.DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    lookup_field="id"

# GENERICVIEWSET
class BookViewSet(GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request):
        books = self.get_queryset()
        serializer = self.get_serializer(books, many=True)
        print(serializer.data)
        return Response(serializer.data)
        
    def retrieve(self, request, pk=None):
        book = self.get_object()
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        book = self.get_object()
        serializer = self.get_serializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        book = self.get_object()
        self.perform_destroy(book)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # in case of customization
    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
