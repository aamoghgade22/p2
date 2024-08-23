from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Task
from .serializers import StudentSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class =MyTokenObtainPairSerializer


##  MODEL VIEWSET

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    #overriding some method
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

##  GENERIC VIEW SET

# FOR GET , CREATE
class StudentGeneric (generics.ListAPIView,generics.CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
# FOR UPDATE AND DELETE
class StudentGeneric1 (generics.UpdateAPIView,generics.DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    lookup_field="id"