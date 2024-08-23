from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, StudentGeneric, TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'books', BookViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),# automatically creates for books and tasks
]
