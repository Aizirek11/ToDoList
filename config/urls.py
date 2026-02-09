from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet, index
from users.views import UserViewSet, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger / документация
schema_view = get_schema_view(
    openapi.Info(
        title="Task Manager API",
        default_version='v1',
        description="Task Manager backend API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# 🔹 Роутер для tasks и users
router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="tasks")
router.register(r"users", UserViewSet, basename="users")  # пользователи

urlpatterns = [
    # Главная страница — HTML Kanban
    path('', index, name='index'),

    # Админка
    path('admin/', admin.site.urls),

    # регистрация пользователя
    path("api/auth/register/", RegisterView.as_view(), name="register"),

    # JWT login и refresh
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # API через роутер
    path("api/", include(router.urls)),

    # Swagger / Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
