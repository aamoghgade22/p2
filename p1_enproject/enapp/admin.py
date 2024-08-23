from django.contrib import admin
from .models import Student, Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ("id","user","title", "description", "status")
    ordering = ["id"] 
    search_fields = ["user"]

admin.site.register(Task,TaskAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ("id","name", "age", "address","isActive",)
    search_fields = ["name"]
    list_per_page = 10
    ordering = ["id"] 

admin.site.register(Student,StudentAdmin)
