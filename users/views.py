from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UsersSerializer


# ------------------------
# Регистрация пользователя
# ------------------------
class RegisterView(generics.CreateAPIView):
    """
    POST /api/auth/register/
    """
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]  # регистрация доступна всем


# ------------------------
# Просмотр пользователей
# ------------------------
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    GET /api/users/          - список всех пользователей
    GET /api/users/{id}/     - конкретный пользователь
    GET /api/users/me/       - текущий залогиненный пользователь
    """
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [AllowAny]


    @action(detail=False, methods=['get'])
    def me(self, request):
        """
        Возвращает текущего залогиненного пользователя
        """
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
