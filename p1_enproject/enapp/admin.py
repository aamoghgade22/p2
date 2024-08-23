from django.contrib import admin
from .models import Book, Student, Task

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

class BooksAdmin(admin.ModelAdmin):
    list_display = ("title","author", "pages", "language",)
    search_fields = ["title"]
    list_per_page = 10
    ordering = ["id"] 

admin.site.register(Book,BooksAdmin)
