from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from .pagination import TaskPagination
from .permissions import IsOwner

# ===============================
# DRF API для задач
# ===============================
class TaskViewSet(viewsets.ModelViewSet):
    """
    API эндпоинты для задач:
    /api/tasks/       - список и создание
    /api/tasks/{id}/  - детали, обновление, удаление
    """
    pagination_class = TaskPagination
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    # Фильтры, поиск и сортировка
    filterset_fields = ["status", "deadline"]
    search_fields = ["title"]
    ordering_fields = ["created_at"]

    # 🔥 Показываем только задачи текущего пользователя
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    # 🔥 При создании автоматически назначаем owner
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# ===============================
# Фронтенд шаблон Kanban
# ===============================
def index(request):
    """
    Главная страница Kanban-доски
    Карточки будут подтягиваться через API
    """
    return render(request, 'tasks/index.html')

