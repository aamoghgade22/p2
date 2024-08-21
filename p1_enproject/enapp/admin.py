from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ("id","user","title", "description", "status")
    ordering = ["id"] 
    search_fields = ["user"]

admin.site.register(Task,TaskAdmin)