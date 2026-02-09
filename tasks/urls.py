from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, index

# Роутер для DRF API
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', index, name='index'),       # фронтенд — главная страница
    path('api/', include(router.urls)),  # API задачи
]
