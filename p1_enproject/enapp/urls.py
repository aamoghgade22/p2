from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import BookViewSet, CarViewSet, MyTokenObtainPairView, StudentGeneric, StudentGeneric1, TaskViewSet, index

router = DefaultRouter()
router.register(r'books', BookViewSet)#GenericViewSet
router.register(r'tasks', TaskViewSet)#ModelViewSet
router.register(r'cars', CarViewSet)#ModelViewSet

urlpatterns = [
    path('', index, name='index'),  # Home page
    # JWT Authentication URLs
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Generics views for students
    path('student/', StudentGeneric.as_view(), name='student-list'),
    path('student/<id>/', StudentGeneric1.as_view(), name='student-detail'),
    # Router paths for books and tasks
    path('', include(router.urls)),  # This will handle /books and /tasks and /cars using router
]
