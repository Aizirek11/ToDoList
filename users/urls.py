from django.urls import path, include, index
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, UserViewSet

# DRF роутер для пользователей
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    # Регистрация и JWT
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", TokenObtainPairView.as_view(), name="login"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),



    # DRF пользователи
    path("", include(router.urls)),  # /users/ + /users/me/
]
