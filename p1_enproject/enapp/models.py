from django.db import models
from django.conf import settings

class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.title

# FOR GENERICs
class Student(models.Model):
    name=models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField(blank=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
# FOR GENERICVIEWSET
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    language = models.CharField(max_length=30)

    def __str__(self):
        return self.title

# For mixins and genericviewset
class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    def __str__(self):
        return self.name
